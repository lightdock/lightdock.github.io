#!/usr/bin/env python3
import os, re
import argparse
import pandas as pd
from io import StringIO

def parseResultsList(filepath:str) -> pd.DataFrame:
    """Parse solutions.list file into pandas data frame"""

    with open(filepath) as file:
        filelines = file.readlines()

    result = "".join(map(
        lambda line: "\t".join(filter(
            lambda x: x,
            (
                line.replace(
                    pat[0],
                    pat[0].replace(" ", "")
                ) if (pat:=re.findall("\((.*?)\)", line)) else line
            ).split(" ")
        )),
        filelines
    ))

    df = pd.read_csv(
        StringIO(result),
        sep="\t"
    )

    df["Coordinates"] = (
        df["Coordinates"]
        .apply(
            lambda x: tuple(
                float(el)
                for el in x[1:-1].split(",")
            )
        )
    )

    return df.sort_values("Scoring", ascending=False)

if __name__ =="__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("input_solutions_file")
    parser.add_argument("-n", default=10)
    args = parser.parse_args()

    solutionsFilePath =  os.path.abspath(
        args.input_solutions_file
    )
    parentPath = os.path.dirname(
        solutionsFilePath
    )
    finalResultsPath = os.path.join(
        parentPath,
        "top_structures"
    )
    os.mkdir(finalResultsPath)

    df = parseResultsList(solutionsFilePath).head(n=args.n).reset_index(drop=True)

    top_structures = df.apply(
        lambda row: os.path.join(
            parentPath,
            "swarm_%s" % row["Swarm"],
            row["PDB"]
        ),
        axis=1
    ).reset_index()

    top_structures.apply(
        lambda row: os.rename(
            row[0],
            os.path.join(
                finalResultsPath,
                "%s_%s" % (
                    row["index"],
                    os.path.basename(row[0])
                )
            )
        ),
        axis=1
    )