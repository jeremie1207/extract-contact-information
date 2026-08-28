# extract-contact-information-cli

A Python command-line tool that extracts **email addresses and phone numbers from a web page**.

## 📌 Project Overview

The goal of this project is to build a CLI tool that accepts a URL, downloads the corresponding web page, extracts its textual content, searches for contact information, and saves the results to an output.

The project is inspired by the classic "Phone Number and Email Address Extractor" automation project, but instead of reading text from the clipboard, this version works directly with web pages.

### Example use case

You are given a company website and want to quickly find all publicly available contact information.

Instead of manually searching through the page, you could run:

```text
contact-extractor https://example.com
```

The tool would analyze the page and produce an output containing the contact information it discovered.

---

## ✨ Core Features

### 1. Accept a URL

The application must accept a web page URL as an argument.

Example:

```text
contact-extractor https://example.com
```

The URL should be validated before attempting to retrieve the page.

---

### 2. Retrieve the web page

The application should make an HTTP request to the supplied URL.

It should handle common problems such as:

- Invalid URLs
- DNS failures
- Connection failures
- HTTP errors
- Timeouts
- Pages that cannot be accessed

The program should provide a useful error message instead of crashing with an unhandled exception.

###

---

### 3. Find email addresses

The application should search the extracted page content for email addresses.

For example, it should be able to identify addresses such as:

```text
contact@example.com
support@example.org
john.doe@company.ca
```

The same email address may appear multiple times on a page.

The output should avoid unnecessary duplicates.

---

### 4. Find phone numbers

The application should search the page content for phone numbers.

The extractor should consider common phone-number formats rather than assuming that every number follows exactly the same pattern.

Examples of formats that could be considered:

```text
613-555-1234
613.555.1234
613 555 1234
(613) 555-1234
+1 613 555 1234
+1-613-555-1234
```

The project should clearly define which formats are supported.

---

### 5. Generate an output

The extracted contact information should be written to an output.

A possible output structure could be:

```text
Emails
------
contact@example.com
support@example.org

Phone Numbers
-------------
+1 613 555 1234
(613) 555-5678
```

The exact format is part of the project design and can be improved as you develop the application.

---

## 🖥️ CLI Design

The application should behave like a real command-line utility.

### Basic command

```text
contact-extractor <URL>
```

### Possible options

As an extension, consider supporting options such as:

```text
--emails-only
--phones-only
--verbose
```

For example:

```text
contact-extractor https://example.com --emails-only
```

Start with the simplest possible CLI and add functionality incrementally.

#

---

## 🔒 Scope

The application should only process publicly accessible web pages and should not attempt to bypass authentication, access controls, CAPTCHAs, or other technical restrictions.
