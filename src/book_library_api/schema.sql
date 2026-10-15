CREATE DATABASE IF NOT EXISTS book_library;

USE book_library;

DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS user_tokens;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

CREATE TABLE `users` (
    `user_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
    `username` varchar(255) NOT NULL,
    `password_hash` varchar(255) NOT NULL,
    PRIMARY KEY (`user_id`),
    UNIQUE KEY `users_user_id_uk` (`user_id`),
    UNIQUE KEY `users_username_uk` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb3;

CREATE TABLE `user_tokens` (
    `user_token_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
    `user_id` int(11) unsigned NOT NULL,
    `access_token` varchar(255) NOT NULL,
    `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `expired_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`user_token_id`),
    UNIQUE KEY `user_tokens_user_token_id_uk` (`user_token_id`),
    KEY `user_tokens_users_user_id_fk` (`user_id`),
    CONSTRAINT `user_tokens_users_user_id_fk` FOREIGN KEY (`user_id`)
    REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb3;

CREATE TABLE `books` (
    `book_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
    `user_id` int(11) unsigned NOT NULL,
    `title` varchar(255) NOT NULL,
    `pages` int(11) unsigned NOT NULL DEFAULT 0,
    `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`book_id`),
    UNIQUE KEY `books_book_id_uk` (`book_id`),
    KEY `books_users_user_id_fk` (`user_id`),
    CONSTRAINT `books_users_user_id_fk` FOREIGN KEY (`user_id`)
    REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb3;

CREATE TABLE `authors` (
    `author_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
    `user_id` int(11) unsigned NOT NULL,
    `name` varchar(255) NOT NULL,
    `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`author_id`),
    UNIQUE KEY `authors_author_id_uk` (`author_id`),
    KEY `authors_users_user_id_fk` (`user_id`),
    CONSTRAINT `authors_users_user_id_fk` FOREIGN KEY (`user_id`)
    REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb3;

CREATE TABLE `book_authors` (
    `book_author_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
    `book_id` int(11) unsigned NOT NULL,
    `author_id` int(11) unsigned NOT NULL,
    PRIMARY KEY (`book_author_id`),
    UNIQUE KEY `book_authors_book_author_id_uk` (`book_author_id`),
    KEY `book_authors_books_book_id_fk` (`book_id`),
    KEY `book_authors_authors_author_id_fk` (`author_id`),
    CONSTRAINT `book_authors_books_book_id_fk` FOREIGN KEY (`book_id`)
    REFERENCES `books` (`book_id`) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT `book_authors_authors_author_id_fk` FOREIGN KEY (`author_id`)
    REFERENCES `authors` (`author_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb3;
