from zipfile import *
import os
import shutil

def main():

    file_name = "Programming Food List.docx"

    zip_archive = ZipFile ( file_name );

    zip_archive.extract( "word/document.xml",u"\\\\?\\D:\\Programming Competition\\ProgrammingCompetition2016");

    

    zip_archive.close();

    extracted_folder = "word/document.xml"
    moved_file = "document.xml"
    os.rename(extracted_folder, moved_file)
    shutil.rmtree("word")




    
    zip_archive = ZipFile ( file_name, "w" );

    object_handle = open(moved_file);
    object_handle.write();
    

    

if( __name__ == "__main__"):
    main();
