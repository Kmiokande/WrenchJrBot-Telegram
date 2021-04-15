# 🤖 WrenchJrBot

![Wrench Jr](./media/wrenchjr_banner.jpg)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/python-telegram-bot)
![GitHub issues](https://img.shields.io/github/issues/Kmiokande/WrenchJrBot-Telegram)
![GitHub closed issues](https://img.shields.io/github/issues-closed/Kmiokande/WrenchJrBot-Telegram)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Kmiokande/WrenchJrBot-Telegram)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/Kmiokande/WrenchJrBot-Telegram)
![GitHub contributors](https://img.shields.io/github/contributors/Kmiokande/WrenchJrBot-Telegram)
![Lines of code](https://img.shields.io/tokei/lines/github/Kmiokande/WrenchJrBot-Telegram)
![GitHub](https://img.shields.io/github/license/Kmiokande/WrenchJrBot-Telegram)
![GitHub Repo stars](https://img.shields.io/github/stars/Kmiokande/WrenchJrBot-Telegram?style=social)
![GitHub forks](https://img.shields.io/github/forks/Kmiokande/WrenchJrBot-Telegram?style=social)

## Installation

First clone the project and install requirements.

```shell
$ git clone https://github.com/Kmiokande/WrenchJrBot-Telegram.git
$ cd WrenchJrBot-Telegram
$ pip install -r requirements.txt
```

## Using with Docker

We are going to build an image using our Dockerfile. To do this, we use the ```docker build``` command.

The build command optionally takes a ```--tag``` flag. The tag is used to set the name of the image and an optional tag in the format ```name:tag```. We’ll leave off the optional ```tag``` for now to help simplify things. If you do not pass a tag, Docker uses “latest” as its default tag.

```shell
docker build --tag wrenchjr-docker .
```

To run an image inside of a container, we use the ```docker run``` command.

```shell
docker run wrenchjr-docker
```

## License

Licensed under the GNU General Public License v3.0. See [`LICENSE`](LICENSE) for more details.
