%define module	BeautifulSoup 
  
Summary:	The Screen-Scraper's Friend 
Name:		python2-beautifulsoup
Version:	3.2.2
Release:	1
Epoch:		1
Group:		Development/Python
License:	Python
Url:		https://www.crummy.com/software/BeautifulSoup 
Source0:	https://files.pythonhosted.org/packages/40/f2/6c9f2f3e696ee6a1fb0e4d7850617e224ed2b0b1e872110abffeca2a09d4/BeautifulSoup-3.2.2.tar.gz
BuildArch:	noarch 
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python2)
%rename		python-beautifulsoup
 
%description 
The BeautifulSoup class turns arbitrarily bad HTML into a tree-like 
nested tag-soup list of Tag objects and text snippets. A Tag object 
corresponds to an HTML tag.  It knows about the HTML tag's attributes, 
and contains a representation of everything contained between the 
original tag and its closing tag (if any). It's easy to extract Tags 
that meet certain criteria. 
  
%prep
%setup -qn %{module}-%{version}
  
%install 
PYTHONDONTWRITEBYTECODE= %__python2 setup.py install --root=%{buildroot} 

%files
%{python2_sitelib}/Bea*

