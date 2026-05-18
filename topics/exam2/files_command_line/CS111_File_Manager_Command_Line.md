# CS 111 – File Manager & Command Line 

---

# File Manager (GUI)

A file manager is a program that allows you to view, organize, and manage the files and folders on your computer. 
It provides a visual way to navigate the file system, move and rename files, create folders, and access stored information.

**File Explorer** (Windows) and Finder(Macintosh) are two examples of file managers.

Take a few minutes to use the File Manager 

* Navigation
* Views
* File properties
* Paths
* Right-click or Command-click on a file to see properties such as file size and date created



# Part 1 - Using the File Manager

## 1. Extract the Sample Files

1. Download [`cs111_files.zip`](cs111_files.zip)
2. Move it to your **Documents** folder
3. Extract the file:

### Windows

* Open **File Explorer**
* Navigate to **Documents**
* Right-click `cs111_files.zip`
* Select **Extract All…**
* Click **Extract**
* A folder named `cs111_files` should appear

### Mac

* Open **Finder**
* Navigate to **Documents**
* Double-click `cs111_files.zip`
* macOS will automatically extract it
* A folder named `cs111_files` will appear

4. Open the folder `cs111_files`

---

## 2. Inspect the Files

Open the folder `cs111_files`.

---

### A. Count the Files

* Look at the bottom of the File Manager window for total items.
* If you do not see a count:

**Windows**

* Click inside the folder
* Look at the bottom status bar
* Or press `Ctrl + A` to select all and view item count

**Mac**

* Press `Command + A`
* The item count appears at the bottom of the Finder window

**Answer:**
How many files are in this folder?

---

### B. Identify File Types

Switch to a detailed view:

**Windows**

* Click **View**
* Choose **Details**
* If file extensions are not visible:

  * Click **View → Show → File name extensions**

**Mac**

* Click **View → as List**
* Right-click column header and enable **Kind**
* Or press `Command + J` and enable “Show item info”

Look for:

* `.docx`
* `.pdf`
* `.pptx`
* `.xlsx`
* `.jpg`

**Answer:**

* How many of each file type?
* What does the file extension tell you?

---

## 3. Sort the Files

Sort the files by:

### Sort by Name

**Windows:** Click the **Name** column header
**Mac:** Click the **Name** column

* What is first?
* What is last?

### Sort by Type (Kind)

**Windows:** Click the **Type** column
**Mac:** Click the **Kind** column

* How many of each file type?

### Sort by Date Modified

**Windows:** Click **Date modified**
**Mac:** Click **Date Modified**

* What is newest?
* What is oldest?

> 💡 Sorting reveals file metadata (information stored about files).

---

## 4. Organize by Type

Inside `cs111_files`, create folders:

* `Documents`
* `Spreadsheets`
* `Presentations`
* `Images`

### Create Folder

**Windows:** Right-click → **New → Folder**
**Mac:** Right-click → **New Folder**

Move files into their folders:

* `.docx` + `.pdf` → Documents
* `.xlsx` → Spreadsheets
* `.pptx` → Presentations
* `.jpg` → Images

---

## 5. Search Using Wildcards

Use the search bar in the `cs111_files` folder.

Try:

```
*Texas*
*.docx
*.jpg
```

### Windows Tip

* Make sure you are searching **This Folder**

### Mac Tip

* Click **“cs111_files”** under “Search:” to limit results to the folder

**Answer:**

* How many files contain “Texas”?
* How many `.docx` files?
* What does `*` represent?

---

## 6. Cleanup (GUI)

Delete the folders you created:

**Windows**

* Right-click folder → **Delete**

**Mac**

* Right-click folder → **Move to Trash**

Keep:

* `cs111_files.zip`
* The original `cs111_files` folder

---

# Part 2 — Command Line (Terminal)

In Part 2, you will recreate the same folder organization
using the command line instead of the File Manager.


Before starting Part 2, make sure the folder `cs111_files`
contains only the original files (no subfolders).
If needed, delete the folders you created in Part 1.


---

## 1. Open Terminal

**Windows**

* Search for **Windows Terminal** or **cmd**
* Or open **Command Prompt**

**Mac**

* Open **Terminal** (Applications → Utilities → Terminal)

---

## 2. Navigate to the Folder

### Windows

```
cd %USERPROFILE%\Documents\cs111_files
```

### Mac

```
cd ~/Documents/cs111_files
```

If you get an error:

* Check spelling
* Use `dir` (Windows) or `ls` (Mac) to confirm location

---

## 3. List Files

### Windows

```
dir
dir *Texas*
```

### Mac

```
ls
ls *Texas*
```

What files matched `*Texas*`?

---

## 4. Create Folders

```
mkdir Documents Spreadsheets Presentations Images
```

Verify:

**Windows**

```
dir
```

**Mac**

```
ls
```

---

## 5. Move Files Using Wildcards

### Windows

```
move *.docx Documents
move *.pdf Documents
move *.xlsx Spreadsheets
move *.pptx Presentations
move *.jpg Images
```

### Mac

```
mv *.docx Documents
mv *.pdf Documents
mv *.xlsx Spreadsheets
mv *.pptx Presentations
mv *.jpg Images
```

Verify the folders now contain the correct files.

---

## 6. Cleanup (CLI)

Delete the folders you created:

### Windows

```
rmdir Documents
rmdir Spreadsheets
rmdir Presentations
rmdir Images
```

### Mac

```
rmdir Documents
rmdir Spreadsheets
rmdir Presentations
rmdir Images
```

If folders are not empty, you moved files incorrectly.

---

# Reflection

1. Which was faster for organizing files: File Manager or Terminal?
2. Why might programmers prefer command-line tools?
3. How does wildcard `*` help manage many files at once?

---

# Common Command Line Commands (Windows & Mac)

| Task                        | Windows (CMD / PowerShell)      | Mac (Terminal / Bash / zsh)   | Description                |
| --------------------------- | ------------------------------- | ----------------------------- | -------------------------- |
| Change directory            | `cd Documents`                  | `cd Documents`                | Move into a folder         |
| Move up one level           | `cd ..`                         | `cd ..`                       | Go back one directory      |
| List files                  | `dir`                           | `ls`                          | Show files and folders     |
| List matching files         | `dir *.pdf`                     | `ls *.pdf`                    | Show matching files        |
| Create folder               | `mkdir MyFolder`                | `mkdir MyFolder`              | Create directory           |
| Move file(s)                | `move *.pdf Documents`          | `mv *.pdf Documents`          | Move files                 |
| Copy file                   | `copy file.txt Backup\file.txt` | `cp file.txt Backup/file.txt` | Copy file                  |
| Delete file                 | `del file.txt`                  | `rm file.txt`                 | Delete file                |
| Delete all files            | `del *.*` ⚠                     | `rm *` ⚠                      | Delete all files           |
| Remove empty folder         | `rmdir MyFolder`                | `rmdir MyFolder`              | Remove empty folder        |
| Remove folder with contents | `rmdir /s MyFolder` ⚠           | `rm -r MyFolder` ⚠            | Delete folder and contents |

⚠ Important:

* There is no recycle bin in the command line.
* Always check your location with `dir` or `ls` first.

---

-- end --