# Archiving Endangered Videos on the Internet
## Mission Statement
This is GitHub guide and tool meant to advise archivists on archiving endangered films currently on the internet storage at institutions. In this project, we are defining "endangered" films as those only streaming on relatively unstable platforms such as YouTube, and are out of print on physical media. This project could also apply to other video-hosting platforms but is currently untested.

This project outputs a Sumbission Information Package (SIP) for ingestation into an institution according to the Library of Congress' [Bag-it](https://datatracker.ietf.org/doc/html/rfc8493) specification. 

<details>
 <summary>Here is a truncated explanation on SIPs and Bag-it</summary>


## Submission Information Packages (SIP)
* SIPs include the data (payload) and all of the related metadata about the content of the payload.
* It also includes a manifest of every file in the payload with its corresponding checksum.
* You can can include descriptive elements that provide context such as provenance, contact information, environment of creation, etc.
* SIPs can also have a README file with any additional information that should exist alongside the data.
* You can think of SIPs as the file(s) and all the information one would need to facilitate future use.

## BagIt Structure:
* A set of required and optional tag files.
* A subdirectory named "data" called the payload directory.
* A set of optional tag directories.
* The tag files in the base directory consist of one or more files named "**manifest-algorithm.txt**", a file named "**bagit.txt**", and zero or more additional tag files.
</details>
## Disclaimers
Downloading films from YouTube is a violation of their Terms of Service, but not illegal. Under U.S. [Copyright Law Section 107](https://www.law.cornell.edu/uscode/text/17/107), "the fair use of a copyrighted work, including such use by reproduction in copies or phonorecords or by any other means specified by that section, for purposes such as criticism, comment, news reporting, teaching (including multiple copies for classroom use), scholarship, or research, is not an infringement of copyright." This project is not applicable to materials that can be found on the secondhand market.

This process is only known to be permissible under U.S. Law. The fair use analysis that justifies your download of a video is only valid if you live in the U.S. or a territory. Otherwise, it is incumbent upon you to determine whether or not your country allows for fair use. 

## Security
The orignal youtube-dl repo is blocked. In order to download videos from YouTube using the Command Line, yt-dlp (a fork of youtube-dl) must be used. Most of the tools are third-party ones downloaded via command-line, which may be blocked depending on your institution's IT policies. 

YouTube has the right to block your account for violating their Terms of Service. If using yt-dlp, it is best not to use an institution's official computer or YouTube account. If this is done at significant scale, there is a chance you may be blocked from YouTube.

### Prerequisites
**Hardware**
A Linux or MacOS computer with a browser installed as well as a YouTube account.

**Software**
* [Homebrew](https://brew.sh/) is a package-manager needed to install many application via command-line **(MacOS only)**.
* [FFMPEG](https://ffmpeg.org/download.html) is needed by to get the best possible quality file, in whatever file extension you want. 
* [yt-dlp](https://github.com/yt-dlp/yt-dlp) yt-dlp is a command-line video downloader need to archive these videos. 
* [Python](https://www.python.org/) is needed on either platform to run Library of Congress' Bag-it Python library and the automated metadata script.
* [Bagit-Python](https://github.com/LibraryOfCongress/bagit-python) is required to make our downloaded files into a Bag.


## Prerequisites Installation (MacOS)
If you do not have it installed already, install Homebrew by opening the Terminal app and typing or pasting the following:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

You may need to input your password for the admin user.

Next install ffmpeg:
```
brew install ffmpeg
```

After installing ffmpeg you can install yt-dlp:
```
brew install yt-dlp
```

Now python:
```
brew install python
```

Last but not least, install Bagit:
```
pip install bag-it
```
## Prerequisites Installation (Linux)

Install ffmpeg by typing or copying the following:
```
sudo apt install ffmpeg
```
**Python Install**
Next, check if Python is already installed:
```
python3 -v
```
If no version appears e.g. `3.X.X`, you can install python by doing this:
```
sudo apt-get install python`
```
Next, create a new python virtual environment :
```
python -m env python-env
```

Activate your newly created virtual environment:
```
source python-env/bin/activate
```
(**FYI** this step needs to be taken every session prior to downloading the video.)

After activating, you can install yt-dlp:
```
pip install yt-dlp
```
And finally Bagit:

```
pip install bag-it
```

### Using yt-dlp
**CHECK FOR UPDATES:**
Before running yt-dlp, ensure that you are on the latest version of yt-dlp. If you are on MacOS that just means typing the following:
```
brew upgrade yt-dlp
```
On Linux make sure to activate your Python virtual environment:
```
source python-env/bin/activate
```
Then check for updates:
```
pip install --upgrade yt-dlp
```
**Cookies (yum):**
If the video is age-restricted, or you are worried about the possiblity of being banned from youtube, it is adviseable to follow this [tutorial](https://github.com/yt-dlp/yt-dlp/wiki/Extractors) on how to export your cookies from browser. Most browsers do not allow you to export your cookies out directly, so you will need to install an extension on your browser. Whatever name is exported, make sure the file is renamed `cookies.txt`.

To download a video type the following:
```
yt-dlp -P path/to/folder --write-info-json --restrict-filenames example "https://exampleurl.com"
```
Or feed yt-dlp cookies:
```
yt-dlp -P path/to/folder --write-info-json example --cookies cookies.txt "https://exampleurl.com"
```
This command will download the video into a folder, but make sure to replace `path/to/folder` to a specified directory. Also make sure to replace `https://exampleurl.com` with a link to your YouTube video. It puts the yt-dlp metadata in a json next to the downloaded video which will then be used in the bagging process. 

### Bag that Bidya

Now that we have our video and metadata downloaded, we need to put them in a Bag. We can do this after installing bag-it by typing the following commmand:
```
bagit.py --contact-name 'Firstname Lastname' /directory/to/bag
```

`Firstname Lastname` should be replaced with your first and last name, and `/directory/to/bag`, the directory to your bag.

**NOTE:** If you are a Linux user make sure you are activated into your python virtual environment.

Next download this [python script](https://github.com/miapmiapmiap/Preserving-Endangered-Media-Guide/blob/main/yt-dlp_bagit.py) If you want to do this in command-line you can copy this:
```
wget https://raw.githubusercontent.com/miapmiapmiap/Preserving-Endangered-Media-Guide/refs/heads/main/yt-dlp_bagit.py
```

Run the script by typing the following:
```
python yt-dlp_bagit.py
```

The script will automatically ask you a series of questions, so make sure to be as precise as possible.

Below are the questions and some sample answers, replace the answers with your own:
```
What is the directory to your bag?
example_directory
```
```
What is your email?
example@example.com
```
```
"Please describe the data in the bags (e.g. Youtube video and associated metadata from filmmaker Maurice Chevalier.) 
Youtube video and associated metadata file by filmmaker Simba Pride
```
```
Please write the name of the institution you work for.
CIA
```
```
Please input the address of the institution you work for.
110 Ganef Ave, Seattle, Washington, 22244
```

The script will automatically edit the `bag-info.txt`, save and generate new checksums.

Now you are done! Feel free to ingest the bagged-folder into your institution's system. 

