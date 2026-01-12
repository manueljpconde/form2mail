# contact.py

from fastapi import APIRouter, Request, Form, UploadFile, File
from fastapi.responses import JSONResponse
from app.models.contact import ContactForm
from app.services.email_service import send_email
from typing import Optional
import logging

router = APIRouter()

@router.post("/send-email/")
async def send_contact_email(
    name: str = Form(..., max_length=100),
    email: str = Form(...),
    phone: Optional[str] = Form(None, max_length=20),
    consent_ts: Optional[str] = Form(None, max_length=50),
    subject: str = Form(..., max_length=150),
    message: str = Form(..., max_length=2000),
    file: UploadFile = File(None),
    request: Request = None
):
    try:
        # Create ContactForm instance
        contact_form = ContactForm(
            name=name,
            email=email,
            phone=phone,
            consent_ts=consent_ts,
            subject=subject,
            message=message
        )
        
        # Log validated form data
        logging.info(f"Validated form data: {contact_form.dict()}")

        # Attempt to send the email
        await send_email(contact_form, file)

        # Return success response
        return {"status": "success", "message": "Message sent successfully"}

    except Exception as e:
        # Log the error
        logging.error(f"Error sending email: {str(e)}")

        # Return a JSON response with the error message
        return JSONResponse(
            status_code=200,
            content={
                "error": "Server Error",
                "message": "There was an issue sending your message. Please try again later."
            }
        )
