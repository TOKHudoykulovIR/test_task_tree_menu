## Instructions: How to Use

Follow these steps to set up and run your Django project:

1. Apply database migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

2. Create a superuser for the admin panel:
    ```bash
    python manage.py createsuperuser
    ```

3. Open the Django admin panel and add new data (menu, menu items).

## Example Usage

Here's an example of how to use the endpoints:

```bash
# Get list of menu
curl http://127.0.0.1:8000/list-menu/

# Get details for menu with ID 1
curl http://127.0.0.1:8000/list-menu/1
