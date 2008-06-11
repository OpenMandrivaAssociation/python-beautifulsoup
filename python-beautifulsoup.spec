%define oname	BeautifulSoup 
  
Name:		python-beautifulsoup 
Version:	3.0.6
Release:	%mkrel 1
Summary:	The Screen-Scraper's Friend 
  
Group:		Development/Libraries 
License:	Python
URL:		http://www.crummy.com/software/BeautifulSoup 
Source0:	http://www.crummy.com/software/BeautifulSoup/download/%{oname}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root 
  
BuildArch:	noarch 
BuildRequires:	python-devel
BuildRequires:	python-setuptools
Requires:	python 
  
%description 
The BeautifulSoup class turns arbitrarily bad HTML into a tree-like 
nested tag-soup list of Tag objects and text snippets. A Tag object 
corresponds to an HTML tag.  It knows about the HTML tag's attributes, 
and contains a representation of everything contained between the 
original tag and its closing tag (if any). It's easy to extract Tags 
that meet certain criteria. 
  
%prep
%setup -q -n %{oname}-%{version}
  
%build 
  
%install 
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --compile --optimize=2

%clean 
rm -rf %{buildroot}
  
%files  
%defattr(-,root,root,-) 
%{py_puresitedir}/%{oname}.py*
%{py_puresitedir}/%{oname}Tests.py*
%{py_puresitedir}/%{oname}-%{version}-py%{pyver}.egg-info

