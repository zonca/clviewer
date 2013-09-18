Interactive visualization of CMB Angular power spectrum plots
($C_l$) pasted to github gists.

Paste a gist number, i.e. the last component of a gist address (integer):

<form onsubmit="location.href='/' + document.getElementById('myInput').value; return false;">
  <input type="text" id="myInput" />
  <input type="submit" />
</form>

Usage:

* Paste any number of files to a github gist, first
column is $\ell$, second column is $C_{\ell}$, space separated, example:

    <http://gist.github.com/zonca/6599016>

* Paste the gist number (i.e. 6599016) in the form at <http://clviewer.herokuapp.com>, or use direct URL, example:

    <http://clviewer.herokuapp.com/zonca/6599016>

 
* The `python` application parses the content of the gists and produces an interactive plot,
using the filename as the label for each curve

