#!/usr/bin/python3
import argparse
import os
import sys
import GwentUtils

from datetime import datetime
import CardData
import KeywordData
import CategoryData

parser = argparse.ArgumentParser(description="Transform the Gwent card data contained in xml files into a "
                                             "standardised JSON format. See README for more info.",
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("inputFolder", help="unzipped data_definitions.zip. Folder containing the xml files.")
parser.add_argument("-l", "--language", help="Includes just the translations for the selected language. Results in much smaller json files. Choose from: en-US, de-DE, es-ES, es-MX, fr-FR, it-IT, ja-JP, ko-KR, pl-PL, pt-BR, ru-RU, zh-CN, zh-TW")
args = parser.parse_args()
rawFolder = args.inputFolder
locale = args.language
if locale:
    GwentUtils.LOCALES = [locale]

# Add a backslash on the end if it doesn't exist.
if rawFolder[-1] != "/":
    rawFolder = rawFolder + "/"

if not os.path.isdir(rawFolder):
    print(rawFolder + " is not a valid directory")
    exit()

gwentDataHelper = GwentUtils.GwentDataHelper(rawFolder)

BASE_FILENAME = datetime.utcnow().strftime("%Y-%m-%d") + ".json"

print("Creating keyword JSON...")
keywordsJson = KeywordData.create_keyword_json(gwentDataHelper)
filename = "keywords_" + BASE_FILENAME
filepath = os.path.join(rawFolder + "../" + filename)
GwentUtils.save_json(filepath, keywordsJson)

print("Creating categories JSON...")
categoriesJson = CategoryData.create_category_json(gwentDataHelper)
filename = "categories_" + BASE_FILENAME
filepath = os.path.join(rawFolder + "../" + filename)
GwentUtils.save_json(filepath, categoriesJson)

print("Creating card data JSON...")
cardsJson = CardData.create_card_json(gwentDataHelper)
filename = "cards_" + BASE_FILENAME
filepath = os.path.join(rawFolder + "../" + filename)
print("Found %s cards." % (len(cardsJson)))
GwentUtils.save_json(filepath, cardsJson)
