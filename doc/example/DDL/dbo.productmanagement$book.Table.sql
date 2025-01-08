USE [OnlineBookStore];

/**** Lorem ipsum dolor 234 #$% ****/

CREATE TABLE [dbo].[productmanagement$book] (
    [id] [int] PRIMARY KEY,
    [title] [varchar](255) NOT NULL,
    [price] [decimal](10, 2),
    [publicationyear] [year]
);