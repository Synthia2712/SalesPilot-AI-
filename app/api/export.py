from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.services.export_service import ExportService

router = APIRouter(
    prefix="/export",
    tags=["Export"],
)


@router.get("/")
def export():

    filename = ExportService.export()

    return FileResponse(
        filename,
        filename=filename,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )