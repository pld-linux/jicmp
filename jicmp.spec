
Summary:	Java interface to the ICMP protocol
Summary(pl.UTF-8):	Iterfejs Javy do protokołu ICMP
Name:		jicmp
Version:	1.0.10
Release:	0.1
License:	GPL
Group:		Libraries/Java
Source0:	http://dl.sourceforge.net/opennms/%{name}-%{version}.tar.gz
URL:		http://www.opennms.org/index.php/Jicmp
BuildRequires:	jpackage-utils
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JICMP is a Java interface to the ICMP protocol (ping), originally
written as a part of OpenNMS.

%description -l pl.UTF-8
JICMP to interfejs Javy do protokołu ICMP (ping), pierwotnie napisany
jako część OpenNMS.

%package devel
Summary:	Development files for JICMP
Summary(pl.UTF-8):	Pliki deweloperskie dla JICMP
Group:		Development/Libraries

%description devel
Development files for JICMP

%description devel -l pl.UTF-8
Pliki deweloperskie dla JICMP

%prep
%setup -q

%build
export JAVA_HOME="%{java_home}"

required_jars="jaxp_parser_impl"
CLASSPATH=$(build-classpath $required_jars)
export CLASSPATH

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root)  %{_libdir}/lib%{name}.so
%{_javadir}/*.jar

%files devel
%defattr(644,root,root,755)
%attr(755,root,root)  %{_libdir}/lib%{name}.la
