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
export TWILIO_AUTH_TOKEN=5b2f1b22d610f2a571d6a5df6c931611
export TWILIO_PHONE_NUMBER=+12604758637