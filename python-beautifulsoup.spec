%define module	BeautifulSoup 
  
Name:		python-beautifulsoup
Version:	3.2.1
Release:	1
Summary:	The Screen-Scraper's Friend 
Group:		Development/Python
License:	Python
URL:		http://www.crummy.com/software/BeautifulSoup 
Source0:	http://www.crummy.com/software/BeautifulSoup/download/%{module}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root 
BuildArch:	noarch 
BuildRequires:	python-devel
BuildRequires:	python-setuptools
  
%description 
The BeautifulSoup class turns arbitrarily bad HTML into a tree-like 
nested tag-soup list of Tag objects and text snippets. A Tag object 
corresponds to an HTML tag.  It knows about the HTML tag's attributes, 
and contains a representation of everything contained between the 
original tag and its closing tag (if any). It's easy to extract Tags 
that meet certain criteria. 
  
%prep
%setup -q -n %{module}-%{version}
  
%install 
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean 
%__rm -rf %{buildroot}
  
%files -f FILE_LIST
%defattr(-,root,root,-) 

