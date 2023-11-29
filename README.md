# Enhanced Contact Management System

## Overview
Building upon our previous CLI contact management system, this enhanced version introduces birthday management, robust data validation, and pagination for large address books. It uses object-oriented programming principles for efficient and organized data handling.

## New Features
- **Birthday Management**:
  - `Birthday` field to store the contact's birthday.
  - `days_to_birthday` method in `Record` to calculate days until the next birthday.
- **Data Validation**:
  - Enhanced validation for phone numbers and birthday entries.
  - Setter and getter logic for `value` attributes in `Phone` and `Birthday`.
- **Pagination in AddressBook**:
  - Iterator implementation for displaying address book entries in paginated format.

## Core Classes
- **Field**: Base class for entry fields, now including `Birthday`.
- **Name, Phone**: Classes for storing contact's name and phone numbers, with validation.
- **Record**: Manages contact info, including name, multiple phone numbers, and birthday.
- **AddressBook**: Inherits from `UserDict`, manages records, and implements pagination.

## Functionality
- **AddressBook Pagination**:
  - Implements an iterator method for viewing large address books in parts.
  - Each iteration returns a representation of `N` records.
- **Record**:
  - Additional (optional) `Birthday` argument.
  - `days_to_birthday` method to calculate the days until the next birthday if provided.
- **Validation Logic**:
  - Ensures correct phone number format in `Phone`.
  - Validates and handles birthday data in `Birthday`.

## Installation
Clone the repository and ensure Python is installed. This application requires no external dependencies.
