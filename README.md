## Pasos para la instalación

### Crear un ambiente virtual después de la clocanción
```bash
python3 -m venv venv
```

### instalar paquetes necesarios
```bash
pip install -r requirements.txt
```

### Migrar los models creados con AlchemySQL 
- Ubicarse dentro del directorio principal FlaskAPI/ desde la terminal y correr el siguiente comando
   - Este comando crea el directorio migrations/ en nuestro projecto el cual inicializa el proceso de migración
    ```bash
    python -m flask --app src/models/UsersModel.py db init 
    ```
   - El siguiente comando crea el archivo de mapeo para la creación de la base de datos (el sql que se va a ejecutar)
    ```bash
    python -m flask --app src/models/UsersModel.py db migrate 
    ```
    - El siguiente comando la base de datos en caso que no exista error en los 2 comandos anteriores
    ```bash
    python -m flask --app src/models/UsersModel.py db upgrade 
    ```
   -El siguiente comando se usa para actualizar cualqueir cambio realizado en la base de datos
    ```bash
    python -m flask --app src/models/UsersModel.py db stamp head
    python -m flask --app src/models/UsersModel.py db migrate 
    python -m flask --app src/models/UsersModel.py db upgrade 
    ```

    ### Realizar el cambio en todos los modelos ubicados en el directorio 'models/' (Pruebas hechas en Mac)
    ```bash
    find ./src/models -type f | grep -v '__' | while read file; do flask --app $file db stamp head; done;
    ```