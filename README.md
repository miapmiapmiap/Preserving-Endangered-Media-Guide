# Archiving Endangered Films on the Internet

## Mission Statement
This GitHub guide is meant to advise archivists in archiving endangered films currently on the internet. In this project, we are defining "endangered" films as those only streaming on relatively unstable platforms such as YouTube, and are out of print on physical media. This project could also apply to other platforms such as Vimeo or Internet Archive, but we will focus on YouTube for the sake of brevity.

## Disclaimers

## Legality
Downloading films from YouTube is a violation of their Terms of Service, but not illegal. Under U.S. [Copyright Law Section 107](https://www.law.cornell.edu/uscode/text/17/107), "the fair use of a copyrighted work, including such use by reproduction in copies or phonorecords or by any other means specified by that section, for purposes such as criticism, comment, news reporting, teaching (including multiple copies for classroom use), scholarship, or research, is not an infringement of copyright." This project is not applicable to materials that can be found on the secondhand market.

## Security
youtube-dl is blocked on GitHub. In order to download videos from YouTube using the Command Line, yt-dlp (a fork of youtube-dl) must be used. Also, downloading age restricted videos requires an extension, adding another layer of fallibility.

YouTube has the right to block your account for violating their Terms of Service. If using yt-dlp, it is best not to use an institution's official computer or YouTube account. Using an incognito window to generate cookies is highly reccomended. [Here](https://github.com/yt-dlp/yt-dlp/wiki/Extractors#po-token-guide) is a tutorial on how to do that.

### Prerequisites
**Hardware**
A Linux or MacOS computer with a browser installed as well as a YouTube account.

**Software**
* [Homebrew](https://brew.sh/) is a package-manager needed to install many application via command-line on MacOS.
* [FFMPEG](https://ffmpeg.org/download.html) is needed by to get the best possible quality file, in whatever file extension you want. 
* [yt-dlp](https://github.com/yt-dlp/yt-dlp) yt-dlp is a command-line video downloader need to archive these videos. 
* [Python](https://www.python.org/) is needed on eithier platform to run Library of Congress' Bag-it Python library and the automated metadata script.
* [Bagit-Python](https://github.com/LibraryOfCongress/bagit-python) is required to make our downloaded files into a Bag.


## MacOS
If you do not have it installed already, install Homebrew by opening the Terminal app and typing or pasting the following:

$ `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

You may need to input your password for the admin user.

Next install ffmpeg:
$ `brew install ffmpeg`

After installing ffmpeg you can install yt-dlp:
$ `brew install yt-dlp`

Now python:
$ `brew install python`

Last but not least, install Bagit:
$ `pip install bag-it


# Installing FFMPEG
**To install FFMPEG:**
$ `sudo apt install ffmpeg`

# Installing Python

**To install python:**
$ `sudo apt-get install python3.13.0`

**If python is installed but software cannot find it, use:**
$ `sudo apt install python-is-python3`

**A virtual Python environment must be created:**
$ `python3 -m env python-env`

**Then activate:**
$ `source python-env/bin/activate`

**Once the Python environment is activated, this command installs yt-dlp:**
$ `pip3 install yt-dlp`

**If the video is age-restricted, and the browser is not installed, cookies must be exported and downloaded. An example command would be:**
$ `yt-dlp --cookies example.txt --write-info-json example "https://exampleurl.com"`

**If the video is age-restricted, and the browser is installed, an example command would be:**
$ `yt-dlp --cookies-from-browser examplebrowser --write-info-json example "htpps://exampleurl.com"`

###MacOS
FFMPEG is required to properly run yt-dlp

**To install FFMPEG:**


**If the video is age-restricted, and the browser is not installed, cookies must be exported and downloaded. An example command would be:**
$ `yt-dlp --cookies example.txt --write-info-json example "https://exampleurl.com"`

**If the video is age restricted, and the browser is installed, an example command would be:**
$ `yt-dlp --cookies-from-browser examplebrowser --write-info-json example "https://exampleurl.com"`

**A video downloaded using yt-dlp will output the highest quality .mkv. If specified in the command (--write-info-json), a .json can be output. Do not transcode additonal files. For the purpose of archiving these videos, a .mkv file with copies is sufficient.**
**An example command would be:**
$ `yt-dlp --cookies-from-browser examplebrowser --write-info-json- example "https://exampleurl.com" --postprocessor-args "ffmpeg:-bitexact"`

**Before each session, run:**
$ `brew upgrade yt-dlp`

## Metadata 

### Submission Information Packages (SIP)
* SIPs include the data (payload) and all of the related metadata about the content of the payload.
* It also includes a manifest of every file in the payload with its corresponding checksum.
* You can can include descriptive elements that provide context such as provenance, contact information, environment of creation, etc.
* SIPs can also have a README file with any additional information that should exist alongside the data.
* You can think of SIPs as the file(s) and all the information one would need to facilitate future use.

### BagIt Structure:
* A set of required and optional tag files.
* A subdirectory named "data" called the payload directory.
* A set of optional tag directories.
* The tag files in the base directory consist of one or more files named "**manifest-algorithm.txt**", a file named "**bagit.txt**", and zero or more additional tag files.

### BagIt Guide:

**Download content (video and .json) to specific folder.**

**Install BagIt:**
* **(Mac)** `brew install bagit`
* **(Linux)** `pip install bagit`

**Setup and conform folder to BagIt:**
**Example:**
`bagit.py --source-organization 'organizationexample' --organization-address 'addressexample' --contact-name 'nameexample' --contact-email 'example@gmail.com' --external-description 'descriptionexample' --bag-count '1 of 1'`


