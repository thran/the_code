from pathlib import Path


def filter_dictionary(source_file: Path, target_file: Path, length=5):

    with source_file.open() as input_file, target_file.open('w') as output_file:
        words_processed, words_found = 0, 0
        for line in input_file:
            words_processed += 1
            word = line.strip().split('/')[0].lower()
            if len(word) != 5 or not word.isalpha():
                continue
            output_file.write(f'{word}\n')
            words_found += 1

        print(f'processed: {words_processed}')
        print(f'found: {words_found}')


if __name__ == '__main__':
    LANGUAGE = 'en'
    LENGTH = 5

    filter_dictionary(
        Path(f'{LANGUAGE}.txt'),
        Path(f'{LANGUAGE}-{LENGTH}.solutions.txt'),
        LENGTH
    )
