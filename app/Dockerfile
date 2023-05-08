FROM python:3.8

WORKDIR /Users/macbookdejuan/Library/CloudStorage/OneDrive-Personal/Code/Platzi/Python_Back_End/PIP_y_entornos_virtuales/py-project/app/
COPY requirements.txt /Users/macbookdejuan/Library/CloudStorage/OneDrive-Personal/Code/Platzi/Python_Back_End/PIP_y_entornos_virtuales/py-project/app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /Users/macbookdejuan/Library/CloudStorage/OneDrive-Personal/Code/Platzi/Python_Back_End/PIP_y_entornos_virtuales/py-project/app/requirements.txt

COPY . /Users/macbookdejuan/Library/CloudStorage/OneDrive-Personal/Code/Platzi/Python_Back_End/PIP_y_entornos_virtuales/py-project/app/

CMD bash -c "while true; do sleep 1; done"
