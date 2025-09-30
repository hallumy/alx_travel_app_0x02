# 🏡 Listings App – Django

The `listings` app manages property listings, bookings, and reviews for a travel rental platform.

---

## 📁 Models

### 🏘️ Listing

Represents a property listed by a host.

| Field           | Type         | Description                      |
|----------------|--------------|----------------------------------|
| `property_id`   | UUID         | Primary key                      |
| `host`          | ForeignKey   | References `User`                |
| `name`          | CharField    | Property name (required)         |
| `description`   | TextField    | Property description             |
| `location`      | CharField    | City/location (required)         |
| `price_per_night`| DecimalField| Price per night (required)       |
| `created_at`    | DateTimeField| Auto timestamp on creation       |
| `updated_at`    | DateTimeField| Auto-updated on change           |

---

### 📅 Booking

Tracks user bookings on listings.

| Field         | Type         | Description                          |
|--------------|--------------|--------------------------------------|
| `booking_id` | UUID         | Primary key                          |
| `property`   | ForeignKey   | References `Listing`                 |
| `user`       | ForeignKey   | References `User`                    |
| `start_date` | DateField    | Start of booking                     |
| `end_date`   | DateField    | End of booking                       |
| `total_price`| DecimalField | Total cost for the stay              |
| `status`     | ChoiceField  | One of: `pending`, `confirmed`, `canceled` |
| `created_at` | DateTimeField| Auto timestamp on creation           |

---

### ⭐ Review

Captures user feedback on listings.

| Field        | Type         | Description                           |
|-------------|--------------|---------------------------------------|
| `review_id` | UUID         | Primary key                           |
| `property`  | ForeignKey   | References `Listing`                  |
| `user`      | ForeignKey   | References `User`                     |
| `rating`    | IntegerField | Rating from 1 to 5                    |
| `comment`   | TextField    | User's written review                 |
| `created_at`| DateTimeField| Auto timestamp on creation            |

---

## 🔧 Seed Command

### What is it?

A Django custom management command that populates the database with **sample listings** for development and testing.

What It Does

Creates a default host user (hostuser) if not already present.

Adds 5 sample listings with:

Random titles

Descriptions

Locations (e.g. New York, SF)

Random price per night
