#!/bin/bash
# Setup Environment

## Enter Python Virtual Environment
source venv/bin/activate

## Customized shell prompt
source ./.bash_prompt

## Flask server for dev
export FLASK_APP=app.py

## TWILIO Tokens
export TWILIO_ACCOUNT_SID=ACddf438d1ac80ac3cb4206dec8f545970
export TWILIO_AUTH_TOKEN=8592abc64da19bc8eaeea74d102846da
export TWILIO_PHONE_NUMBER=+12604758637