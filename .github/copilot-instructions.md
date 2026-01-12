# Form2Mail Copilot Instructions

## Architecture Overview
Form2Mail is a FastAPI-based contact form processor that validates submissions and sends emails via SMTP. Key components:
- **Routes** (`app/routes/contact.py`): Handle HTTP endpoints, e.g., `/send-email/` accepts multipart/form-data with contact fields and optional file attachment, validates fields and calls email service
- **Services** (`app/services/email_service.py`): Business logic like email sending using `aiosmtplib`
- **Models** (`app/models/contact.py`): Pydantic models for data validation, e.g., `ContactForm` with name, email, phone (optional), consent_ts (optional), subject, message
- **Middleware** (`app/middleware/api_key_auth.py`): API key authentication via `x-api-key` header
- **Config** (`app/config/settings.py`): CORS origins and environment loading

Data flows: Form submission → Pydantic validation → Async email send → SMTP delivery with Reply-To set to configurable REPLY_TO_EMAIL or submitter's email.

## Developer Workflows
- **Setup**: Run `./install_and_start_dependencies.sh` (creates venv, installs deps from `requirements.txt`, starts server) or manually: `python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt && uvicorn main:app --host 0.0.0.0 --port 3081`
- **Run**: `uvicorn main:app --host 0.0.0.0 --port 3081` (port 3081 is project-specific)
- **Test Endpoint**: Use cURL/Postman with `x-api-key` header and multipart/form-data matching contact form fields (name, email, subject, message, optional phone, consent_ts, file)
- **Debug**: Check logs for validation errors (logged in `main.py` exception handler with request body and errors) and email send failures

## Project Conventions
- **Error Handling**: Always return HTTP 200 with JSON error details (e.g., `{"error": "Server Error", "message": "..."}`) instead of 4xx/5xx codes
- **Email Format**: Sender as `"Contact Form <{EMAIL_SENDER}>"`, Reply-To as configurable REPLY_TO_EMAIL or submitter's email, body formatted with contact details, optional file attachment
- **Async Operations**: Use `async`/`await` for email sending (aiosmtplib)
- **Environment Config**: Load all SMTP/API settings from `.env` (SMTP_SERVER, SMTP_PORT=465, EMAIL_SENDER, EMAIL_RECEIVER, EMAIL_PASSWORD, REPLY_TO_EMAIL, API_KEY)
- **Validation**: Strict Pydantic fields with max lengths (e.g., message: 2000 chars)
- **CORS**: Allow specific origins only (configured in `settings.py`)

## Integration Points
- **SMTP**: Requires external SMTP server (e.g., PrivateEmail); uses SSL on port 465, no STARTTLS
- **External Deps**: `aiosmtplib` for async email, `email-validator` for email validation
- **Auth**: API key from `.env`; middleware allows OPTIONS preflight requests
- **Logging**: Use `logging` module for info/error messages throughout app

Reference `README.md` for full setup and usage examples.</content>
<parameter name="filePath">/Users/mjpc/Play/manueljpconde/form2mail/.github/copilot-instructions.md