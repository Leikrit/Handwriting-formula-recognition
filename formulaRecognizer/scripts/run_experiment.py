from argparse import Namespace
from typing import List, Optional

import hydra
import torch
from omegaconf import DictConfig
from pytorch_lightning import Trainer
from pytorch_lightning.callbacks import Callback, EarlyStopping, ModelCheckpoint
from pytorch_lightning.loggers.wandb import WandbLogger

from image_to_latex.data import Im2Latex
from image_to_latex.lit_models import LitResNetTransformer


@hydra.main(config_path="../conf", config_name="config")
def main(cfg: DictConfig):
    datamodule = Im2Latex(**cfg.data)
    datamodule.setup()

    lit_model = LitResNetTransformer(**cfg.lit_model)
    # lit_model = LitResNetTransformer.load_from_checkpoint(
    #     r"C:\Users\65344\PycharmProjects\image-to-latex-main\scripts\outputs\2023-12-13\12-31-03\wandb\run-20231213_123106-2cluo51m\files\image-to-latex\2cluo51m\checkpoints\epoch=1-val\loss=0.06-val\cer=0.02.ckpt"
    # )

    callbacks: List[Callback] = []
    if cfg.callbacks.model_checkpoint:
        callbacks.append(ModelCheckpoint(**cfg.callbacks.model_checkpoint))
    if cfg.callbacks.early_stopping:
        callbacks.append(EarlyStopping(**cfg.callbacks.early_stopping))

    logger: Optional[WandbLogger] = None
    if cfg.logger:
        logger = WandbLogger(**cfg.logger)

    trainer = Trainer(**cfg.trainer, callbacks=callbacks, logger=logger)

    if trainer.logger:
        trainer.logger.log_hyperparams(Namespace(**cfg))

    trainer.tune(lit_model, datamodule=datamodule)
    trainer.fit(lit_model, datamodule=datamodule)
    trainer.test(lit_model, datamodule=datamodule)


if __name__ == "__main__":
    # torch.backends.cudnn.enabled = True
    #
    # torch.backends.cudnn.benchmark = True
    with torch.no_grad():
        main()
