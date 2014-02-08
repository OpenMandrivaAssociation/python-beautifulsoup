%define module	BeautifulSoup 
  
Name:		python-beautifulsoup
Version:	3.2.1
Release:	2
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



%changelog
* Fri Feb 17 2012 Lev Givon <lev@mandriva.org> 3.2.1-1
+ Revision: 776132
- Force rebuild.
- Update to 3.2.1.

* Tue Jul 19 2011 Lev Givon <lev@mandriva.org> 3.2.0-1
+ Revision: 690678
- Update to 3.2.0.

* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 3.0.8-3
+ Revision: 667913
- mass rebuild

* Fri Oct 29 2010 Funda Wang <fwang@mandriva.org> 3.0.8-2mdv2011.0
+ Revision: 589932
- rebuild for python 2.7

* Fri Jan 08 2010 Emmanuel Andry <eandry@mandriva.org> 3.0.8-1mdv2010.1
+ Revision: 487779
- New version 3.0.8

* Thu Dec 25 2008 Adam Williamson <awilliamson@mandriva.org> 3.0.7a-1mdv2009.1
+ Revision: 318653
- rebuild for python 2.6
- new release 3.0.7a

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 3.0.6-2mdv2009.0
+ Revision: 269019
- rebuild early 2009.0 package (before pixel changes)

* Thu Jun 12 2008 Adam Williamson <awilliamson@mandriva.org> 3.0.6-1mdv2009.0
+ Revision: 218265
- fix group
- br python-setuptools
- switch to using tarball and setuptools-based install system
- small spec clean
- new release 3.0.6

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Mar 12 2007 Crispin Boylan <crisb@mandriva.org> 3.0.3-1mdv2007.1
+ Revision: 142128
- New version
- Dont install into arch dependent lib

* Tue Dec 05 2006 Jérôme Soyer <saispo@mandriva.org> 2.1.1-2mdv2007.1
+ Revision: 91373
- Rebuild for latest python
- Import python-beautifulsoup

* Tue Apr 11 2006 Jerome Soyer <saispo@mandriva.org> 2.1.1-1mdk
- First build

