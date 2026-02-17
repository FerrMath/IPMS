# Inventory & Product Management System
<br/>

**Languages:** English | [português](./README.pt.md)
<br/>
## Project description

A system for managing a store’s inventory and product data. It tracks stock changes, validates product entries, and blocks operations on discontinued products. The system focuses on maintaining data consistency and easy stock control.

## Features

- Track stock levels for each product.
- Validate product information before updates or additions.
- Prevent selling products marked as discontinued.
- Basic categorization of products.
- Record stock changes (e.g., sales, restocking).

## Tech Stack

### Backend

- **Language:** Python
- **Framework:** Flask – handles routing, API endpoints, and basic request/response logic.
- **Database:** MySQL – stores product, stock, and category information.
- **ORM:** SQLAlchemy – maps database tables to Python objects and manages queries.
- **Migrations:** Alembic – handles database schema changes safely over time.

### Frontend

- **Templating:** Jinja – generates dynamic HTML pages using backend data.
- **Markup & Styling:** HTML and CSS – basic layout and styling.
- **Interactivity:** JavaScript – minimal client-side functionality.

### Future Frontend Updates

- Replace or complement Jinja templates with **React** for a more dynamic and responsive UI.
- Use React components to handle product listing, stock updates, and form validation.