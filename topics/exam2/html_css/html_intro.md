---

# Introduction To HTML

---

## HTML

Web pages are created using a language called **Hyper Text Markup Language (HTML)**. The current version of HTML is known as **HTML5**.

The [HTML5 Specification](https://html.spec.whatwg.org/multipage/) is a great reference for everything about HTML. You may want to visit this site after completing this introduction.

For a more general (and complete) introduction to HTML visit [W3 Schools](http://w3schools.com).

The [World Wide Web Consortium (W3C)](http://www.w3.org) promotes web standards. Visit this site for the latest news and trends related to HTML and web technologies.

---

## Basic Concepts

A web page is simply a text file with formatting codes called **tags**. A text editor such as Notepad can be used to create the page. Pages are saved in text format with a file name extension of either `.htm` or `.html`. A web browser is used to display or *render* the HTML.

There are many tools available for creating web pages. Essentially you only need a **text editor** and a **web browser** to create and view web pages locally on your laptop or desktop.

> **Note:** All of the following software options are **free** and can be used to create web pages. Some offer additional features/services for a fee, but are not needed for our course assignments.

### Cloud Editors (No Installation Required)

* [jsfiddle.net](https://jsfiddle.net/)
* [jsbin.com](https://jsbin.com/)
* [replit.com](https://replit.com/)

### Local Laptop/Desktop Text Editors

* [Phoenix (fork of Brackets)](https://phcode.io/) (Mac & Windows)
* [Notepad++](https://notepad-plus-plus.org/) (**Windows - Use in Huntington Indiana Lab**)
* [BBEdit](https://www.barebones.com/products/bbedit/)
* [Atom](https://atom.io/) (Mac & Windows)

> Note: Built-in editors like Notepad (Windows) and TextEdit (Mac) can be used but do not offer syntax highlighting.

### Web Browsers

* [Chrome](http://www.google.com/chrome)
* [Firefox](http://www.mozilla.com/en-US/firefox/)
* [Microsoft Edge](https://www.microsoft.com/en-us/edge)
* [Safari](http://www.apple.com/safari/)

Each browser may render a page slightly differently. It is important to test your pages with multiple browsers and versions.

### Creating a Web Page – Basic Steps

1. Create and edit the HTML file (e.g., `basic.html`)
2. Open the file in a web browser
3. Repeat until satisfied

---

## Web Page Template

Each HTML page uses the following basic structure:

```
<html>

<head>
<title>Web Page Title</title>
</head>

<body>

</body>

</html>
```

HTML documents use `<tags>` to describe structure and content. A tag:

* Has a name
* Is surrounded by `<` and `>`
* Usually has both a beginning and ending tag
* Ending tags use a forward slash: `</tag>`

An HTML document begins with `<html>` and ends with `</html>`.

Content goes between `<body>` tags. Setup information (including `<title>`) goes inside `<head>`.

A complete starter template:

```
<!DOCTYPE html>
<html lang="en">

<head>
<title>Untitled</title>
</head>

<body>

</body>

</html>
```

**Key Concept:**

* HTML defines **content and structure**
* CSS defines **formatting and appearance**

It is best practice to separate structure and formatting.

![HTML vs CSS](images/html_vs_css_sm.png)

---

## Title

The `<title>` tag controls the text shown at the top of the browser. It belongs inside the `<head>` section.

```
<head>
<title>HTML Introduction</title>
</head>
```

Title viewed with Chrome (Windows):

![Title in Chrome](images/ChromeTitle.jpg)

Title viewed with Microsoft Edge (Windows):

![Title in Microsoft Edge](images/EdgeTitle.jpg)

---

## Headings

Headings range from `<h1>` to `<h6>`.

```
<h1>heading size one</h1>
<h2>heading size two</h2>
<h3>heading size three</h3>
<h4>heading size four</h4>
<h5>heading size five</h5>
<h6>heading size six</h6>
```

Headings create document structure:

* `<h1>` = main page title
* `<h2>` = major sections
* `<h3>` and below = subsections

---

## Paragraphs and Breaks

The **paragraph tag `<p>`** creates sections of text. A blank line appears automatically between paragraphs.

Extra spaces and blank lines in HTML source code are ignored.

The **break tag `<br>`** moves text to the next line without adding extra spacing.

Example:

```
<p>This is a paragraph that has
a break here<br>
and another break here<br>
and this is the last line.</p>
```

---

## Strong and Emphasis

The `<strong>` tag indicates importance (usually bold).

The `<em>` tag indicates emphasis (usually italics).

```
This <strong>word</strong> uses strong.
This <em>word</em> uses emphasis.
```

Use `strong` and `em` instead of `<b>` and `<i>` when possible.

---

## Lists

Unordered lists use `<ul>` and ordered lists use `<ol>`. List items use `<li>`.

```
<ul>
  <li>item one</li>
  <li>item two</li>
  <li>item three</li>
</ul>

<ol>
  <li>item one</li>
  <li>item two</li>
  <li>item three</li>
</ol>
```

Rendered:

* item one
* item two
* item three

1. item one
2. item two
3. item three

---

## Web Links

Links use the `<a>` (anchor) tag with the `href` attribute.

```
<a href="http://www.huntington.edu">
Huntington University
</a>
```

Example:

[Huntington University](http://www.huntington.edu)

To link to another page in your project:

```
<a href="css_intro.html">CSS Intro</a>
```

---

## Images

Images use the `<img>` tag.

```
<img src="hulogo.jpg" alt="Huntington University Logo">
```

* `src` specifies the file
* `alt` provides alternate text
* No closing tag is required

Example:

![Huntington University Logo](images/hulogo.jpg)

If the image fails to load, the alt text appears:

![Huntington University Logo](images/hulogobad.jpg)

Resize with width:

```
<img src="hulogo.jpg" width="200">
```

Example:

![Huntington University Logo](images/hulogo_200.jpg)

---

## Validating HTML

To ensure your HTML is correct, validate it at:

[http://validator.w3.org/](http://validator.w3.org/)

Fix the first error (or two), then revalidate. The total number of errors shown may not be accurate.

---

-- end --
