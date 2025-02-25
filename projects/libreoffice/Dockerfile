# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
################################################################################

FROM gcr.io/oss-fuzz-base/base-builder
# enable source repos
RUN sed -i -e '/^#\s*deb-src.*\smain\s\+restricted/s/^#//' /etc/apt/sources.list
#build requirements
RUN apt-get update && apt-get build-dep -y libreoffice
RUN apt-get install -y wget yasm locales && locale-gen en_US.UTF-8
#xenial gperf too old
RUN sed -i -e 's/xenial/bionic/g' /etc/apt/sources.list
RUN apt-get update && apt-get install gperf

#cache build dependencies
ADD https://dev-www.libreoffice.org/src/c74b7223abe75949b4af367942d96c7a-crosextrafonts-carlito-20130920.tar.gz \
    https://dev-www.libreoffice.org/src/e7a384790b13c29113e22e596ade9687-LinLibertineG-20120116.zip \
    https://dev-www.libreoffice.org/src/Amiri-0.111.zip \
    https://dev-www.libreoffice.org/src/ReemKufi-0.7.zip \
    https://dev-www.libreoffice.org/src/edc4d741888bc0d38e32dbaa17149596-source-sans-pro-2.010R-ro-1.065R-it.tar.gz \
    https://dev-www.libreoffice.org/src/907d6e99f241876695c19ff3db0b8923-source-code-pro-2.030R-ro-1.050R-it.tar.gz \
    https://dev-www.libreoffice.org/src/source-serif-pro-3.000R.tar.gz \
    https://dev-www.libreoffice.org/src/liberation-narrow-fonts-ttf-1.07.6.tar.gz \
    https://dev-www.libreoffice.org/src/1725634df4bb3dcb1b2c91a6175f8789-GentiumBasic_1102.zip \
    https://dev-www.libreoffice.org/src/33e1e61fab06a547851ed308b4ffef42-dejavu-fonts-ttf-2.37.zip \
    https://dev-www.libreoffice.org/src/368f114c078f94214a308a74c7e991bc-crosextrafonts-20130214.tar.gz \
    https://dev-www.libreoffice.org/src/liberation-fonts-ttf-2.00.4.tar.gz \
    https://dev-www.libreoffice.org/extern/f543e6e2d7275557a839a164941c0a86e5f2c3f2a0042bfc434c88c6dde9e140-opens___.ttf \
    https://dev-www.libreoffice.org/src/noto-fonts-20171024.tar.gz \
    https://dev-www.libreoffice.org/src/amiri-0.109.zip \
    https://dev-www.libreoffice.org/src/ttf-kacst_2.01+mry.tar.gz \
    https://dev-www.libreoffice.org/src/ReemKufi-0.6.tar.gz \
    https://dev-www.libreoffice.org/src/Scheherazade-2.100.zip \
    https://dev-www.libreoffice.org/src/EmojiOneColor-SVGinOT-1.3.tar.gz \
    https://dev-www.libreoffice.org/src/culmus-0.133.tar.gz \
    https://dev-www.libreoffice.org/src/libre-hebrew-1.0.tar.gz \
    https://dev-www.libreoffice.org/src/alef-1.001.tar.gz \
    https://dev-www.libreoffice.org/src/a8c2c5b8f09e7ede322d5c602ff6a4b6-mythes-1.2.4.tar.gz \
    https://dev-www.libreoffice.org/src/5ade6ae2a99bc1e9e57031ca88d36dad-hyphen-2.8.8.tar.gz \
    https://dev-www.libreoffice.org/src/48d647fbd8ef8889e5a7f422c1bfda94-clucene-core-2.3.3.4.tar.gz \
    https://dev-www.libreoffice.org/src/boost_1_75_0.tar.xz \
    https://dev-www.libreoffice.org/src/box2d-2.3.1.tar.gz \
    https://dev-www.libreoffice.org/src/dtoa-20180411.tgz \
    https://dev-www.libreoffice.org/src/expat-2.4.1.tar.bz2 \
    https://dev-www.libreoffice.org/src/libjpeg-turbo-1.5.3.tar.gz \
    https://dev-www.libreoffice.org/src/lcms2-2.11.tar.gz \
    https://dev-www.libreoffice.org/src/0168229624cfac409e766913506961a8-ucpp-1.3.2.tar.gz \
    https://dev-www.libreoffice.org/src/libexttextcat-3.4.5.tar.xz \
    https://dev-www.libreoffice.org/src/1f5def51ca0026cd192958ef07228b52-rasqal-0.9.33.tar.gz \
    https://dev-www.libreoffice.org/src/a39f6c07ddb20d7dd2ff1f95fa21e2cd-raptor2-2.0.15.tar.gz \
    https://dev-www.libreoffice.org/src/e5be03eda13ef68aabab6e42aa67715e-redland-1.0.17.tar.gz \
    https://dev-www.libreoffice.org/src/cppunit-1.15.1.tar.gz \
    https://dev-www.libreoffice.org/src/openldap-2.4.45.tgz \
    https://dev-www.libreoffice.org/src/neon-0.31.2.tar.gz \
    https://dev-www.libreoffice.org/src/e80ebae4da01e77f68744319f01d52a3-pixman-0.34.0.tar.gz \
    https://dev-www.libreoffice.org/src/cairo-1.16.0.tar.xz \
    https://dev-www.libreoffice.org/src/curl-7.71.0.tar.xz \
    https://dev-www.libreoffice.org/src/xmlsec1-1.2.32.tar.gz \
    https://dev-www.libreoffice.org/src/liblangtag-0.6.2.tar.bz2 \
    https://dev-www.libreoffice.org/src/libabw-0.1.3.tar.xz \
    https://dev-www.libreoffice.org/src/libcdr-0.1.7.tar.xz \
    https://dev-www.libreoffice.org/src/libcmis-0.5.2.tar.xz \
    https://dev-www.libreoffice.org/src/libe-book-0.1.3.tar.xz \
    https://dev-www.libreoffice.org/src/libetonyek-0.1.10.tar.xz \
    https://dev-www.libreoffice.org/src/libfreehand-0.1.2.tar.xz \
    https://dev-www.libreoffice.org/src/libmspub-0.1.4.tar.xz \
    https://dev-www.libreoffice.org/src/libmwaw-0.3.19.tar.xz \
    https://dev-www.libreoffice.org/src/libodfgen-0.1.8.tar.xz \
    https://dev-www.libreoffice.org/src/liborcus-0.16.1.tar.bz2 \
    https://dev-www.libreoffice.org/src/libpagemaker-0.0.4.tar.xz \
    https://dev-www.libreoffice.org/src/libpng-1.6.37.tar.xz \
    https://dev-www.libreoffice.org/src/librevenge-0.0.4.tar.bz2 \
    https://dev-www.libreoffice.org/src/libstaroffice-0.0.7.tar.xz \
    https://dev-www.libreoffice.org/src/libvisio-0.1.7.tar.xz \
    https://dev-www.libreoffice.org/src/libwpd-0.10.3.tar.xz \
    https://dev-www.libreoffice.org/src/libwpg-0.3.3.tar.xz \
    https://dev-www.libreoffice.org/src/libwps-0.4.12.tar.xz \
    https://dev-www.libreoffice.org/src/libzmf-0.0.2.tar.xz \
    https://dev-www.libreoffice.org/src/zlib-1.2.11.tar.xz \
    https://dev-www.libreoffice.org/src/poppler-21.01.0.tar.xz \
    https://dev-www.libreoffice.org/src/poppler-data-0.4.10.tar.gz \
    https://dev-www.libreoffice.org/src/mdds-1.7.0.tar.bz2 \
    https://dev-www.libreoffice.org/src/openssl-1.1.1i.tar.gz \
    https://dev-www.libreoffice.org/src/language-subtag-registry-2021-03-05.tar.bz2 \
    https://dev-www.libreoffice.org/src/graphite2-minimal-1.3.14.tgz \
    https://dev-www.libreoffice.org/src/harfbuzz-2.6.0.tar.xz \
    https://dev-www.libreoffice.org/src/glm-0.9.9.7.zip \
    https://dev-www.libreoffice.org/src/icu4c-69_1-src.tgz \
    https://dev-www.libreoffice.org/src/icu4c-69_1-data.zip \
    https://dev-www.libreoffice.org/src/libxml2-2.9.12.tar.gz \
    https://dev-www.libreoffice.org/src/libxslt-1.1.34.tar.gz \
    https://dev-www.libreoffice.org/src/hunspell-1.7.0.tar.gz \
    https://dev-www.libreoffice.org/src/lxml-4.1.1.tgz \
    https://dev-www.libreoffice.org/src/freetype-2.9.1.tar.bz2 \
    https://dev-www.libreoffice.org/src/fontconfig-2.13.91.tar.gz \
    https://dev-www.libreoffice.org/src/libepoxy-1.5.3.tar.xz \
    https://dev-www.libreoffice.org/src/libepubgen-0.1.1.tar.xz \
    https://dev-www.libreoffice.org/src/libnumbertext-1.0.7.tar.xz \
    https://dev-www.libreoffice.org/src/libqxp-0.0.2.tar.xz \
    https://dev-www.libreoffice.org/src/mariadb-connector-c-3.1.8-src.tar.gz $SRC/
#fuzzing dictionaries
ADD https://raw.githubusercontent.com/rc0r/afl-fuzz/master/dictionaries/gif.dict \
    https://raw.githubusercontent.com/rc0r/afl-fuzz/master/dictionaries/jpeg.dict \
    https://raw.githubusercontent.com/rc0r/afl-fuzz/master/dictionaries/png.dict \
    https://raw.githubusercontent.com/rc0r/afl-fuzz/master/dictionaries/tiff.dict \
    https://raw.githubusercontent.com/rc0r/afl-fuzz/master/dictionaries/xml.dict \
    https://raw.githubusercontent.com/rc0r/afl-fuzz/master/dictionaries/html_tags.dict $SRC/
#fuzzing corpuses
ADD https://lcamtuf.coredump.cx/afl/demo/afl_testcases.tgz $SRC/
RUN mkdir afl-testcases && cd afl-testcases/ && tar xf $SRC/afl_testcases.tgz && cd .. && \
    zip -q $SRC/jpgfuzzer_seed_corpus.zip afl-testcases/jpeg*/full/images/* && \
    zip -q $SRC/giffuzzer_seed_corpus.zip afl-testcases/gif*/full/images/* && \
    zip -q $SRC/bmpfuzzer_seed_corpus.zip afl-testcases/bmp*/full/images/* && \
    zip -q $SRC/pngfuzzer_seed_corpus.zip afl-testcases/png*/full/images/*
RUN svn export https://github.com/khaledhosny/ots/trunk/tests/fonts $SRC/sample-sft-fonts/ots
RUN svn export https://github.com/unicode-org/text-rendering-tests/trunk/fonts/ $SRC/sample-sft-fonts/unicode-org
RUN svn export https://github.com/harfbuzz/harfbuzz/trunk/test/shaping/data/in-house/fonts $SRC/sample-sft-fonts/harfbuzz
ADD https://github.com/adobe-fonts/adobe-variable-font-prototype/releases/download/1.001/AdobeVFPrototype.otf $SRC/sample-sft-fonts/adobe
RUN zip -qr $SRC/sftfuzzer_seed_corpus.zip $SRC/sample-sft-fonts
ADD https://dev-www.libreoffice.org/corpus/wmffuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/xbmfuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/xpmfuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/svmfuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/pcdfuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/dxffuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/metfuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/ppmfuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/psdfuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/epsfuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/pctfuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/pcxfuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/rasfuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/tgafuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/tiffuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/hwpfuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/602fuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/lwpfuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/pptfuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/rtffuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/olefuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/cgmfuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/ww2fuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/ww6fuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/ww8fuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/qpwfuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/slkfuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/fodtfuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/fodsfuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/fodgfuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/fodpfuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/xlsfuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/scrtffuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/wksfuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/diffuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/docxfuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/xlsxfuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/pptxfuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/mmlfuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/mtpfuzzer_seed_corpus.zip \
    https://dev-www.libreoffice.org/corpus/htmlfuzzer_seed_corpus.zip $SRC/
#clone source
RUN git clone --depth 1 git://anongit.freedesktop.org/libreoffice/core libreoffice
WORKDIR libreoffice
COPY build.sh $SRC/
