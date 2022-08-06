import praw
import csv
import string
import os
import pandas as pd

"""
Script to update the JSON metadata obtained using PRAW
"""


def updateComments(submissionDB, commentsDB, reddit):
    """
    Adds comments from submissions in submissionsDB to commentsDB 
    commentsDB, submissionsDB: pandas dataframes to read/write to.
    reddit: an instance of PRAW reddit
    Returns a list of submissions whose metadata needs to be updated in submissionDB
    """
    outdatedSubmissions = set()
    dbLength = submissionDB.shape[0]
    for count, submissionID in enumerate(submissionDB.loc[:, "id"]):
        submission = reddit.submission(submissionID)
        comments = submission.comments.list()
        moreCommentsList = []
        #get a list of all comment objects from PRAW
        for comment in comments:
            if isinstance(comment, praw.models.MoreComments):
                comments.extend(comment.comments())
                moreCommentsList.append(comment)
        #remove MoreCommentsObjects after list has been fully expanded.
        for moreCommentsObj in moreCommentsList:
            comments.remove(moreCommentsObj)
        #update comments in DB
        commentIDs = set(commentsDB.loc[:, "id"])
        for comment in comments:
            if not str(comment.id) in commentIDs:
                outdatedSubmissions.add(str(comment.link_id[3:]))
                #commentDB columns: id, author, flair, comment text, created timestamp, link id, 
                #nest_level, parent id, score, stickied, url-only, detoxify prediction
                if comment.author == None:
                    commentsDB.loc[len(commentsDB)] = [comment.id, '[deleted]', None, comment.body, comment.created_utc, comment.link_id, 
                                                  None,comment.parent_id, comment.score, comment.stickied, 0, None]
                else:
                    commentsDB.loc[len(commentsDB)] = [comment.id, comment.author.name, None, comment.body, comment.created_utc, comment.link_id, 
                                                  None,comment.parent_id, comment.score, comment.stickied, 0, None]
        print(f"{count}/{dbLength} submissions processed. {count/dbLength * 100}% complete.")
    return outdatedSubmissions


def updateSubmissions(submissionDB, outdatedSubmissions, reddit):
    """
    Updates the scores and number of commments for all submissions provided in outdatedSubmissions
    submissionDB: a pandas database of submissions
    outdatedSubmissions: an iterable list of submissions to update.
    reddit: the PRAW reddit API object.
    """
    for submissionID in outdatedSubmissions:
        submission = reddit.submission(submissionID)
        submissionDB.loc[submissionDB['id'] == str(submissionID), ['num_comments', 'score']] = [submission.num_comments, submission.score]

def main():
    reddit = praw.Reddit(
        client_id="te1zQI6-rkeT3osIVvIhIg",
        client_secret="qjF82fgY73Gg5y9E1ZzWviXQOjkc9Q",
        password="BhtQ\T!q`d^4$%!\\",
        user_agent="dreamwastaken2-scraper",
        username="dreamwastaken2-GPT2",
    )   
    submissionDB = pd.read_csv('submission.csv', header=0)

    commentsDB = pd.read_csv('comment.csv',header=0)
    print("UPDATING COMMENT METADATA")
    outdatedSubmissions = updateComments(submissionDB, commentsDB, reddit)
    print("UPDATING SUBMISSION METADATA")
    updateSubmissions(submissionDB, outdatedSubmissions, reddit)
    print("WRITING TO CSV")
    commentsDB.to_csv("updatedCommentsDB.csv", index=False)
    submissionDB.to_csv("updatedSubmissionDB.csv", index=False)
if __name__ == '__main__':
    main()