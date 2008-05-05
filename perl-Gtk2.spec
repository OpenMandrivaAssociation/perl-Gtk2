%define module	Gtk2
%define	name	perl-%{module}
%define	version	1.182
%define	release	%mkrel 2
%define perl_glib_require 1.172
%define gtk_require 2.11.0
%define cairo_require 1.00

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl module for the gtk+-2.x library
License:	GPL or Artistic
Group:	  	Development/GNOME and GTK+
Source:		http://prdownloads.sourceforge.net/gtk2-perl/%{module}-%{version}.tar.bz2
Patch7:		Gtk2-gtk_exit.patch
Patch21:	Gtk2-1.038-xset_input_focus.patch
Patch23:	Gtk2-1.023-exception-trapping.patch 
Patch24:	relocations-2.patch
Patch25:	relocations-fixes.patch
URL:		http://gtk2-perl.sf.net/
BuildRequires:	gtk+2-devel >= %gtk_require
BuildRequires:	perl-devel
BuildRequires:	perl-ExtUtils-Depends >= 0.300
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.03
BuildRequires:	perl-Glib >= %perl_glib_require
BuildRequires:	perl-Cairo >= %cairo_require
# for test suite:
BuildRequires:	fontconfig fonts-ttf-dejavu
Requires:	gtk+2
Requires:	libgtk+2 => %gtk_require
Requires:	perl-Glib >= %perl_glib_require
#	(misc) needed by /usr/lib/perl5/vendor_perl/5.8.7/i386-linux/Gtk2/Install/Files.pm
Requires:	perl-Cairo >= %cairo_require
#	Compatibility with mdk <= 9.2:
Conflicts:	drakconf <= 9.3-21mdk
Conflicts:	drakxtools-newt <= 9.3-14mdk
Conflicts:	rpmdrake <= 2.1-24mdk
Conflicts:	userdrake <= 0.92-4mdk
Conflicts:	drakfirsttime <= 0.91-14mdk
Provides:	perl-GTK2 = %{version}-%{release}
Obsoletes:	perl-GTK2 < 0.1
# (tv) libegg's code for status icon was merged in gtk+2.9.x:
Provides:	perl-Gtk2-StatusIcon = %{version}-%{release}
Obsoletes:	perl-Gtk2-StatusIcon <= 0.010
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module provides perl access to the gtk+-2.x library.

Gtk+ is the GIMP ToolKit (GTK+), a library for creating graphical user
interfaces for the X Window System.  GTK+ was originally written for the GIMP
(GNU Image Manipulation Program) image processing program, but is now used by
several other programs as well.

%package doc
Summary: Gtk2 documentation
Group: Books/Computer books

%description doc
This package contains documentation of the Gtk2 module.


%prep
%setup -q -n %{module}-%{version}
%patch7 -p0
%patch21 -p0 -b .tv
%patch23 -p0 -b .except
%patch24 -p0 -b .reloc
%patch25 -p0 -b .relocfix
perl Makefile.PL INSTALLDIRS=vendor
chmod 755 gtk-demo/*.pl examples/*.pl

%build
%make OPTIMIZE="%{optflags}"

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}


%files
%defattr(-, root, root)
%doc AUTHORS LICENSE
%dir %{perl_vendorarch}/%{module}
%{perl_vendorarch}/%{module}.pm
%{perl_vendorarch}/%{module}/*.pm
%{perl_vendorarch}/%{module}/*/*.pm
%{perl_vendorarch}/%{module}/Install
%{perl_vendorarch}/auto/*

%files doc
%defattr(-, root, root)
%doc gtk-demo examples
%{_mandir}/*/*
%dir %{perl_vendorarch}/%{module}
%{perl_vendorarch}/%{module}/*.pod
%{perl_vendorarch}/%{module}/*/*.pod
%{perl_vendorarch}/%{module}/*/*/*.pod


