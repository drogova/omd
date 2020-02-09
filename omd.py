import re


class Game:

    def __init__(self, steps_tree={}):
        self.steps_tree = steps_tree

    def do_step(self, step_id=0):
        step = self.steps_tree.get(step_id, None)
        if step is not None:
            text = step.get('text', None)
            if text is not None:
                print(text)
                options = step.get('options', None)
                if options is not None:
                    option = ''
                    while option not in options:
                        print('Print: {}/{}'.format(*options))
                        option = re.sub('[^A-Z]', '', str(input()).upper())
                    return self.do_step(options[option])


if __name__ == '__main__':
    steps_tree = {
        0: {
            'text':
                ''.join([' EVERYBODY WANTS TO BE A CAT. '.center(80, '='),
                         '\n\n\tWhich cat species are you?',
                         '\n\tPart of the game by Caitlyn Quinn.',
                         '\n\n' + '=' * 80,
                         '\n\nARE YOU READY TO START?']),
            'options': {'YES': 2, 'NO': 1}
        },
        1: {
            'text': ' Bye! See you next time. '.center(80, '='),
            'options': None
        },
        2: {
            'text':
                ''.join(['\n\n' + '=' * 80,
                         '\n\n\tYou wake up in the morning and stretch,' 
                         '\n\tfrom your large paws to the tip of your tail.',
                         '\n\tThe sun is shining on your coat which – what does your coat do, again?',
                         '\n\n' + '=' * 80,
                         '\nCHOOSE OPTION:',
                         '\n1. Absorbs all this wonderful heat – it\' what black fur is best at.',
                         '\n2. My lush golden fur lets me blend in to my surroundings.\n']),
            'options': {'FIRST': 3, 'SECOND': 4}
        },
        3: {
            'text':
                ''.join(['\n\n' + '=' * 80,
                         '\n\n\tAh yes, your inky-black fur absorbs all the heat,' 
                         '\n\tbut makes you a perfect night time predator.',
                         '\n\tWhich is good, because you\'re... what species?',
                         '\n\n' + '=' * 80,
                         '\nCHOOSE OPTION:',
                         '\n1. A black leopard, obviously.',
                         '\n2. Can\'t you tell? I\'m a black jaguar.\n']),
            'options': {'FIRST': 5, 'SECOND': 6}
        },
        4: {
            'text': ''.join(['\n\n' + '=' * 80,
                               '\n\n\tYou are royalty of the savanna – a lion!',
                               '\n\tAs the king or queen of the beasts,',
                               '\n\tyour territory is in the African savanna,',
                               '\n\truling over the vast grasslands.'
                               '\n\n' + ' THE END. '.center(80, '=')]),
            'options': None
        },
        5: {
            'text': ''.join(['\n\n' + '=' * 80,
                               '\n\n\tYou are a leopard, proud and strong, living in the hot savanna in Africa.',
                               '\n\n' + ' THE END. '.center(80, '=')]),
            'options': None
        },
        6: {
            'text': ''.join(['\n\n' + '=' * 80,
                               '\n\n\tYou are a beautiful jaguar, prowling through the South American rain forests.',
                               '\n\n' + ' The end. '.center(80, '=')]),
            'options': None
        },
    }
    Game(steps_tree).do_step()