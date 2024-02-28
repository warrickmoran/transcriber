# transcriber

# install GitHub Cli
type -p yum-config-manager >/dev/null || sudo yum install yum-utils
sudo yum-config-manager --add-repo https://cli.github.com/packages/rpm/gh-cli.repo
sudo yum install gh

## GitHub Documentation
- [Pull Requests](https://docs.github.com/en/pull-requests)
- [Issues](https://docs.github.com/en/issues)
- [gh CLI](https://cli.github.com/manual/)

# Environment Setup 

## Do not run in VENV unless working with different libraries for development
## create virtual environment delete virtual environment 

```
python3 -m venv env && source ./env/bin/activate
```

### deactivate and delete virtual environment

```
deactivate
rm -rv env
```

### delete virtual environment

## upgrade pip

```
python3 -m pip install -U pip wheel setuptools
```

## install dependencies (openai, python-docx)

```
python3 -m pip install -r requirements.txt
```

# Build Application

# Test Application
[PyTest How-To Guide](https://docs.pytest.org/en/latest/how-to/index.html)

```
    python -m pytest
```

# Reduce Audio File size

* Download the latest git build.

'''
$ wget https://johnvansickle.com/ffmpeg/builds/ffmpeg-git-i686-static.tar.xz
$ wget https://johnvansickle.com/ffmpeg/builds/ffmpeg-git-i686-static.tar.xz.md5

'''

* With the build and the build's md5 hash downloaded you can check its integrity.

'''
$ md5sum -c ffmpeg-git-amd64-static.tar.xz.md5
    ffmpeg-git-amd64-static.tar.xz: OK
'''

* Unpack the build. Note: If you need to do this on Windows, use 7-Zip to unpack it. You may have to run it twice; once to uncompress and again to untar the directory.

'''
$ tar xvf ffmpeg-git-amd64-static.tar.xz
'''

* Resize Audio File to meet 25mb OpenAI Whisper Limit [Large File Issue](https://community.openai.com/t/how-do-i-get-whisper-to-allow-larger-files-in-the-request/572288)

'''
./ffmpeg -i <...audio file...> -vn -map_metadata -1 -ac 1 -c:a libopus -b:a 12k -application voip audio.ogg
'''
