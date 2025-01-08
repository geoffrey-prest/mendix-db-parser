USE [OnlineBookStore];

/**** Lorem ipsum dolor 234 #$% ****/

CREATE TABLE [dbo].[productmanagement$review] (
    [id] [int] PRIMARY KEY,
    [rating] [int] CHECK ([rating] BETWEEN 1 AND 5),
    [comment] [text],
    [reviewdate] [datetime]
);