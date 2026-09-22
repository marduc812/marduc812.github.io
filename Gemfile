source "https://rubygems.org"
gem "jekyll"
gem "minima"
gem "webrick"

# Run with:
#   LC_ALL=en_US.UTF-8 bundle exec htmlproofer ./_site --disable-external --checks Images,Links --no-enforce-https
# --no-enforce-https is required: the migrated content has pre-existing
# http:// links from the original WordPress posts, and enforce_https is a
# separate check from --disable-external, so it flags them even with
# external checks off. LC_ALL is required: nokogiri raises
# Encoding::InvalidByteSequenceError on this corpus's curly-quote content
# without a UTF-8 locale.
gem "html-proofer"
