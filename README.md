# marvindv/immich-scripts

## Album2External

Moves all assets in a specified album to another physical location (e.g. the directory of an external library).

Run the following command on your Immich host:

```shell
docker run -t \
  --user "1000:1000" \
  -v /my/library/dir:/my/library/dir \
  -v /mnt/my/external/dir:/mnt/my/external/dir \
  marvindv/immich-scripts album2external \
    --api-key <insert your api key> \
    --api-host http://<insert your immich address>/api \
    --album-name <insert your album name> \
    --host-upload-location /my/library/dir \
    --target-location /mnt/my/external/dir \
    --target-library-name <insert your external library name> \
    --dry-run
```

The user running the script needs to have at least read access to the upload library assets and
read/write access to the target directory, so be sure to adjust the UID and GID in the `--user`
argument.
Since the container needs to access the actual asset files, the source and target directories have
to be bound with `-v`. In this example the path in the container is the same as the one on the host.
You can bind your directories to other paths in the container but be sure to change
`--host-upload-location` and `--target-location` to these paths accordingly.

If everything goes well and no errors are thrown, remove the `--dry-run` argument.

### Run with Poetry

Clone the repository as shown below and run the following command on your Immich host:

```shell
poetry run album2external \
    --api-key <insert your api key> \
    --api-host http://<insert your immich address>/api \
    --album-name <insert your album name> \
    --host-upload-location /my/library/dir \
    --target-location /mnt/my/external/dir \
    --target-library-name <insert your external library name> \
    --dry-run
```

### Motivation

While the introduction of Partner Sharing to Immich is great, it lacks a few feature to be fully usable for my personal use case.
Assets from your partner will not share faces, won't show up on your map and so on.

As discussed on [Reddit](https://www.reddit.com/r/immich/comments/17rs415/partner_share_doesnt_share_everything/) an alternative approach is to use a shared external library by both partner accounts. While this comes with the drawback of duplicated thumbnail generation and individual face recognition, it fits my personal needs. But unlike the proposed method on the linked Reddit discussion of just moving all my assets from my own upload library to the shared external library I want to be able to select the assets to move by adding them to specific album. Running this script with the appropriate parameters allows you to do just that.

## Getting Started

### Prerequisites

- Immich instance running, tested with 1.94.1
- The user running the script needs to have at least read access to the upload library assets and read/write access to the shared external library.
- [Poetry](https://python-poetry.org/docs/#installation) installed

### Installation

```shell
git clone https://github.com/marvindv/immich-scripts.git
cd immich-scripts
poetry install
# Run any of the scripts:
poetry run album2external --help
```

## Acknowledgements

Inspiration on how to use Immichs OpenAPI in Python: https://github.com/alvistar/immich-albums
