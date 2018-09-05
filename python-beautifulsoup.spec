%define module	BeautifulSoup 
  
Summary:	The Screen-Scraper's Friend 
Name:		python2-beautifulsoup
Version:	3.2.1
Release:	10
Epoch:		1
Group:		Development/Python
License:	Python
Url:		http://www.crummy.com/software/BeautifulSoup 
Source0:	http://www.crummy.com/software/BeautifulSoup/download/%{module}-%{version}.tar.gz
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

