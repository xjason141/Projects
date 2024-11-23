<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Php</title>
</head>
<body>
    <?php
        $bookList = [
            'Sorcerer\'s Stone',
            'Gotham\'s Nightmare',
            'A Bad Day'
        ];
        
        $bookdict = [
                [
                    'name' => 'Sorcerer\'s Stone',
                    'author' => 'J.K.Rowling',
                    'purchaseURL' => 'www.example1.com',
                    'releaseYear' => 2020
                ],
                [
                    'name' => 'Gotham\'s Nightmare',
                    'author' => 'Bane Armstrong',
                    'purchaseURL' => 'www.example2.com',
                    'releaseYear' => 2019
                ],
                [
                    'name' => 'A Bad Day',
                    'author' => 'Bane Armstrong',
                    'purchaseURL' => 'www.example3.com',
                    'releaseYear' => 2010
                ],
                [
                    'name' => 'Nightmare\'s End',
                    'author' => 'Jimmy Horson',
                    'purchaseURL' => 'www.example4.com',
                    'releaseYear' => 2010 
                ]
            ];

        // function filterAuth($bookdict, $author) {
        //     $filteredBooks = [];

        //     foreach ($bookdict as $book) {
        //         if ($book['author'] === $author) {
        //             $filteredBooks[] = $book;
        //         }
        //     };

        //     return $filteredBooks;
        // };

        function filters ($data, $key, $value) {

            $filteredData = [];

            foreach ($data as $item) {
                if ($item[$key] === $value) {
                    $filteredData[] = $item;
                }
            };

            return $filteredData;
        };


        function newFilter($data, $fn) {
            $filteredByYear = [];

            foreach ($data as $item) {
                if ($fn($item)) {
                    $filteredByYear[] = $item;
                }
            };
            return $filteredByYear;
        };

        $filterByAuthor = (filters($bookdict, 'author' ,'Bane Armstrong'));
        $filterByYear = (newFilter($bookdict, function ($items) {
            return $items['releaseYear'] < 2020;
        }));
        
    ?>
    <h1>Your Book List</h1>
    <ul>
        <?php foreach ($bookdict as $books) : ?>
            <li><?= $books['name'] ?> written by <?= $books['author'] ?></li>
            <a href="<?= $books['purchaseURL'] ?>"><?= $books['purchaseURL'] ?></a>
        </br>
    </br>
    <?php endforeach ?>      
    </ul>
    <h2>Books written by Bane Armstrong</h2>
        <ul>
            <?php foreach ($filterByAuthor as $book) : ?>
                <li>
                    <?= $book['name'] ?> written by <?= $book['author'] ?>
                    <br>
                    <a href="<?= $book['purchaseURL'] ?>"><?= $book['purchaseURL'] ?></a>
                    <br>
                    <br>
                </li>
            <?php endforeach ?>
        </ul>
    <h2>Books written before 2020</h2>
    <ul>
        <?php foreach ($filterByYear as $byYear) : ?>
            <li>
                <?= $byYear['name'] ?> written by <?= $byYear['author'] ?> (<?= $byYear['releaseYear'] ?>)
                <br>
                <a href="<?= $byYear['purchaseURL'] ?>"><?= $byYear['purchaseURL'] ?></a>
                <br>
                <br>
            </li>                
        <?php endforeach ?>
    </ul>
    </body>
</html>