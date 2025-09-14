from fastapi import APIRouter, File, UploadFile

router = APIRouter(
    prefix="/api/v1/food",
    tags=["/food"]
)

@router.post("/submit")
async def submit_image(image: UploadFile = File(...)):
    image_path = f"/tmp/{image.filename}"
    with open(image_path, "wb") as f:
        f.write(await image.read())

