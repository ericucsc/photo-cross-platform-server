#!/bin/bash
# Setup Environment

## Enter Python Virtual Environment
source venv/bin/activate

## Customized shell prompt
source ./.bash_prompt

## Flask server for dev
export FLASK_APP=app.py

## TWILIO Tokens
source ./.twilio_env