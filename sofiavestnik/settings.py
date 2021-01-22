BOT_NAME = 'sofiavestnik'
SPIDER_MODULES = ['sofiavestnik.spiders']
NEWSPIDER_MODULE = 'sofiavestnik.spiders'
ROBOTSTXT_OBEY = True
LOG_LEVEL = 'WARNING'
ITEM_PIPELINES = {
   'sofiavestnik.pipelines.DatabasePipeline': 300,
}
