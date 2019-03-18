#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-urca
Version  : 1.3.0
Release  : 8
URL      : https://cran.r-project.org/src/contrib/urca_1.3-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/urca_1.3-0.tar.gz
Summary  : Unit Root and Cointegration Tests for Time Series Data
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: R-urca-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
###############
# R E A D M E #
###############
The two files in the `/Rcmdr' directory of urca, namely `Rcmdr-urca.R'
and `Rcmdr-menus.txt', can be utilisied as an add-in to `Rcmdr' of
John Fox. For more information on `Rcmdr' please visit the URL:

%package lib
Summary: lib components for the R-urca package.
Group: Libraries

%description lib
lib components for the R-urca package.


%prep
%setup -q -c -n urca

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552803314

%install
export SOURCE_DATE_EPOCH=1552803314
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library urca
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library urca
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library urca
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  urca || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/urca/CITATION
/usr/lib64/R/library/urca/ChangeLog
/usr/lib64/R/library/urca/DESCRIPTION
/usr/lib64/R/library/urca/INDEX
/usr/lib64/R/library/urca/Licenses/License
/usr/lib64/R/library/urca/Licenses/MacKinnonLicense.txt
/usr/lib64/R/library/urca/Meta/Rd.rds
/usr/lib64/R/library/urca/Meta/data.rds
/usr/lib64/R/library/urca/Meta/features.rds
/usr/lib64/R/library/urca/Meta/hsearch.rds
/usr/lib64/R/library/urca/Meta/links.rds
/usr/lib64/R/library/urca/Meta/nsInfo.rds
/usr/lib64/R/library/urca/Meta/package.rds
/usr/lib64/R/library/urca/NAMESPACE
/usr/lib64/R/library/urca/R/urca
/usr/lib64/R/library/urca/R/urca.rdb
/usr/lib64/R/library/urca/R/urca.rdx
/usr/lib64/R/library/urca/Rcmdr/README
/usr/lib64/R/library/urca/Rcmdr/Rcmdr-menus.txt
/usr/lib64/R/library/urca/Rcmdr/Rcmdr-urca.R
/usr/lib64/R/library/urca/book-ex/Rcode-1-1.R
/usr/lib64/R/library/urca/book-ex/Rcode-1-2.R
/usr/lib64/R/library/urca/book-ex/Rcode-1-3.R
/usr/lib64/R/library/urca/book-ex/Rcode-1-4.R
/usr/lib64/R/library/urca/book-ex/Rcode-2-1.R
/usr/lib64/R/library/urca/book-ex/Rcode-2-10.R
/usr/lib64/R/library/urca/book-ex/Rcode-2-11.R
/usr/lib64/R/library/urca/book-ex/Rcode-2-2.R
/usr/lib64/R/library/urca/book-ex/Rcode-2-3.R
/usr/lib64/R/library/urca/book-ex/Rcode-2-4.R
/usr/lib64/R/library/urca/book-ex/Rcode-2-5.R
/usr/lib64/R/library/urca/book-ex/Rcode-2-6.R
/usr/lib64/R/library/urca/book-ex/Rcode-2-7.R
/usr/lib64/R/library/urca/book-ex/Rcode-2-8.R
/usr/lib64/R/library/urca/book-ex/Rcode-2-9.R
/usr/lib64/R/library/urca/book-ex/Rcode-3-1.R
/usr/lib64/R/library/urca/book-ex/Rcode-3-2.R
/usr/lib64/R/library/urca/book-ex/Rcode-3-3.R
/usr/lib64/R/library/urca/book-ex/Rcode-3-4.R
/usr/lib64/R/library/urca/book-ex/Rcode-4-1.R
/usr/lib64/R/library/urca/book-ex/Rcode-4-2.R
/usr/lib64/R/library/urca/book-ex/Rcode-4-3.R
/usr/lib64/R/library/urca/book-ex/Rcode-4-4.R
/usr/lib64/R/library/urca/book-ex/Rcode-5-1.R
/usr/lib64/R/library/urca/book-ex/Rcode-5-2.R
/usr/lib64/R/library/urca/book-ex/Rcode-5-3.R
/usr/lib64/R/library/urca/book-ex/Rcode-5-4.R
/usr/lib64/R/library/urca/book-ex/Rcode-5-5.R
/usr/lib64/R/library/urca/book-ex/Rcode-6-1.R
/usr/lib64/R/library/urca/book-ex/Rcode-6-2.R
/usr/lib64/R/library/urca/book-ex/Rcode-6-3.R
/usr/lib64/R/library/urca/book-ex/Rcode-7-1.R
/usr/lib64/R/library/urca/book-ex/Rcode-7-2.R
/usr/lib64/R/library/urca/book-ex/Rcode-7-3.R
/usr/lib64/R/library/urca/book-ex/Rcode-8-1.R
/usr/lib64/R/library/urca/book-ex/Rcode-8-10.R
/usr/lib64/R/library/urca/book-ex/Rcode-8-11.R
/usr/lib64/R/library/urca/book-ex/Rcode-8-12.R
/usr/lib64/R/library/urca/book-ex/Rcode-8-13.R
/usr/lib64/R/library/urca/book-ex/Rcode-8-14.R
/usr/lib64/R/library/urca/book-ex/Rcode-8-15.R
/usr/lib64/R/library/urca/book-ex/Rcode-8-16.R
/usr/lib64/R/library/urca/book-ex/Rcode-8-17.R
/usr/lib64/R/library/urca/book-ex/Rcode-8-2.R
/usr/lib64/R/library/urca/book-ex/Rcode-8-3.R
/usr/lib64/R/library/urca/book-ex/Rcode-8-4.R
/usr/lib64/R/library/urca/book-ex/Rcode-8-5.R
/usr/lib64/R/library/urca/book-ex/Rcode-8-6.R
/usr/lib64/R/library/urca/book-ex/Rcode-8-7.R
/usr/lib64/R/library/urca/book-ex/Rcode-8-8.R
/usr/lib64/R/library/urca/book-ex/Rcode-8-9.R
/usr/lib64/R/library/urca/book-ex/ex2.tar.gz
/usr/lib64/R/library/urca/data/Raotbl1.rda
/usr/lib64/R/library/urca/data/Raotbl2.rda
/usr/lib64/R/library/urca/data/Raotbl3.rda
/usr/lib64/R/library/urca/data/Raotbl4.rda
/usr/lib64/R/library/urca/data/Raotbl5.rda
/usr/lib64/R/library/urca/data/Raotbl6.rda
/usr/lib64/R/library/urca/data/Raotbl7.rda
/usr/lib64/R/library/urca/data/UKconinc.rda
/usr/lib64/R/library/urca/data/UKconsumption.rda
/usr/lib64/R/library/urca/data/UKpppuip.rda
/usr/lib64/R/library/urca/data/denmark.rda
/usr/lib64/R/library/urca/data/ecb.rda
/usr/lib64/R/library/urca/data/finland.rda
/usr/lib64/R/library/urca/data/npext.rda
/usr/lib64/R/library/urca/data/nporg.rda
/usr/lib64/R/library/urca/help/AnIndex
/usr/lib64/R/library/urca/help/aliases.rds
/usr/lib64/R/library/urca/help/paths.rds
/usr/lib64/R/library/urca/help/urca.rdb
/usr/lib64/R/library/urca/help/urca.rdx
/usr/lib64/R/library/urca/html/00Index.html
/usr/lib64/R/library/urca/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/urca/libs/urca.so
/usr/lib64/R/library/urca/libs/urca.so.avx2
/usr/lib64/R/library/urca/libs/urca.so.avx512
