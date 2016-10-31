#!/usr/bin/perl

require '../../myTest-lib.pl';
ui_print_header(undef, $text{'index_title'}, "", undef, 1, 1);

print "<!DOCTYPE html>\n";
print "<html>\n";
#
print "<head>\n";
print "<title>Page Title</title>\n";
print "<script>";
print "function myFunction() {
    document.getElementById(\"demo\").innerHTML = \"change from 0017223344556677_Tempratue.cgi.\";
}";
print "</script>";
print "</head>\n";
#
print "<body>\n";

#read input cgi parameters

my  $restful_path;
&ReadParse();
foreach $key (keys %in) {
    print "<p>key= $key, value = $in{$key}</p>\n";
    $restful_path = $key;
};



print "<p id=\"demo\">rsetful_path = $restful_path</p>";
print "<button type=\"button\" onclick=\"myFunction()\">Try it</button>";

print "</body>\n";
print "</html>\n";

ui_print_footer("/", $text{'index'});
