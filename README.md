# Loan Qualifier Application

This is a python command-line interface application that allows users to input income and loan related data and see qualifying loans from lenders quickly and easily. The application works by that taking in a `daily_rate_sheet` of loan criteria from various loan providers, asks the user a number of questions to evaluate their loan eligibility, and then returns to them a list of qualifying loans to be saved to csv file.
---

## Technologies

This project leverages python 3.7 with the following packages:

* [fire](https://github.com/google/python-fire) - For the command line interface, help page, and entrypoint.

* [questionary](https://github.com/tmbo/questionary) - For interactive user prompts and dialogs

* [pytest](https://docs.pytest.org/en/stable/) - For basic assertion testing of financial calculators and filters, and filio.

---

## Installation Guide

Before running the application first install the following dependencies.

```python
  pip install fire
  pip install questionary
  pip install pytest
  pip install mkdocs

```
---

## Examples

To view the user interaction with the tool: https://github.com/allyche/module_2_challenge/blob/main/screen_shot.jpg

---

## Usage

To use the loan qualifier application simply clone the repository and run the **app.py** with:

```python
python app.py
```

---

## Contributors

Brought to you by Ally Che (ally.che@gmail.com)

---

## License

<When you share a project on a repository, especially a public one, it's important to choose the right license to specify others what they can and can not do with your source code and files. Use this section to include the licence you want to use.>