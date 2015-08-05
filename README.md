CppPyDoc is a cpp files parser. The program analyzes the input file and
returns output consisting of the function namespace, function declaration
and its doc string.

Doc string should be embraced as follows:

int TheNS::foo(int a, int b = 0) {
    /*
     * some doc
     */
     return b;
}

The doc string can be also an inline documentation (use "//").

Use:
===
python3 CppPyDoc.py --source="source_file_or_directory" --destination="final_doc_file.csv"
Optional parameter: --recursive: seek for files recursively in directory given in source parameter
