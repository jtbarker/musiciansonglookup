import lyricsgenius
import click


@click.command()
@click.option('--count', default=1, help='Number of songs.')
@click.option('--name', prompt='Artist',
              help='The artist to search.')
def main(name,count):
    """
    :param name: name of artist you want to search
    :param count: how many song results you want to return
    :return: string representation of songs
    """
    clientaccesstoken = 'bringyourowntoken'
    genius = lyricsgenius.Genius(clientaccesstoken)
    artist = genius.search_artist(name, max_songs=count, sort="title")

    click.echo("{}".format(artist.songs))

if __name__ == "__main__":
    main()
