# transcriber

#install GitHub Cli
type -p yum-config-manager >/dev/null || sudo yum install yum-utils
sudo yum-config-manager --add-repo https://cli.github.com/packages/rpm/gh-cli.repo
sudo yum install gh

# create virtual environmemtn 
python3 -m venv env
source env/bin/activate

# upgrade pip
python3 -m pip install --upgrade pip

# install dependencies (openai, python-docx)
python3 -m pip install -r requirements.txt
