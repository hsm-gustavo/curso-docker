FROM python:3.14 as builder

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --user --upgrade -r /code/requirements.txt

FROM python:3.14-slim

WORKDIR /code

COPY --from=builder /root/.local /root/.local

COPY . /code

ENV PATH=/root/.local/bin:$PATH

CMD ["fastapi", "run", "main.py", "--port", "8000"]