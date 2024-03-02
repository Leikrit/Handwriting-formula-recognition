from http import HTTPStatus

import numpy as np
from albumentations.pytorch.transforms import ToTensorV2
from fastapi import FastAPI, File, UploadFile
from PIL import Image

from image_to_latex.lit_models import LitResNetTransformer


app = FastAPI(
    title="Image to Latex Convert",
    desription="Convert an image of math equation into LaTex code.",
)


@app.on_event("startup")
async def load_model():
    global lit_model
    global transform
    lit_model = LitResNetTransformer.load_from_checkpoint("artifacts/model.pt")
    lit_model.freeze()
    transform = ToTensorV2()


@app.get("/", tags=["General"])
def read_root():
    """Health check."""
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": {},
    }
    return response


@app.post("/predict/", tags=["Prediction"])
def predict(file: UploadFile = File(...)):
    image = Image.open(file.file).convert("L")
    image_tensor = transform(image=np.array(image))["image"]  # type: ignore
    pred = lit_model.model.predict(image_tensor.unsqueeze(0).float())[0]  # type: ignore
    decoded = lit_model.tokenizer.decode(pred.tolist())  # type: ignore
    decoded_str = " ".join(decoded)
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": {"pred": decoded_str},
    }
    return response

if __name__ == '__main__':
    corrct = 0
    with open(r"C:\Users\65344\PycharmProjects\image-to-latex-main\processed_data\im2latex_test_filter.lst", 'r',
              encoding='utf-8') as f1:
        line1 = f1.read()
        file_name = line1.split('\n')
        for i in range(11639):
            file = "C:/Users/65344/PycharmProjects/image-to-latex-main/processed_data/all_image/" + file_name[i].split('.')[0] + ".png"
            lit_model = LitResNetTransformer.load_from_checkpoint(
                r"C:\Users\65344\PycharmProjects\image-to-latex-main\scripts\outputs\2023-12-12\19-19-56\wandb\run-20231212_192002-3eih1p26\files\image-to-latex\3eih1p26\checkpoints\epoch=1-val\loss=0.07-val\cer=0.02.ckpt"
            )
            lit_model.freeze()
            transform = ToTensorV2()
            image = Image.open(file).convert("L")
            image_tensor = transform(image=np.array(image))["image"]  # type: ignore
            pred = lit_model.model.predict(image_tensor.unsqueeze(0).float())[0]  # type: ignore
            decoded = lit_model.tokenizer.decode(pred.tolist())  # type: ignore
            decoded_str = " ".join(decoded)
            print(i)
            print(decoded_str)
            print(type(decoded_str), len(decoded_str))
            with open(
                    "C:/Users/65344/PycharmProjects/image-to-latex-main/processed_data/all_label/" + file_name[i].split('.')[0] + ".txt",
                    'r',
                    encoding='utf-8') as f2:
                line = f2.read()
                print(line)
            # print(line == decoded_str)
            if line == decoded_str:
                corrct += 1
        print(corrct)
