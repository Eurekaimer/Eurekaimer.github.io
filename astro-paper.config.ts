import { defineAstroPaperConfig } from "./src/types/config";

export default defineAstroPaperConfig({
  site: {
    url: "https://www.eurekaimer.icu",
    title: "Eurekaimer",
    description: "A quiet personal homepage.",
    author: "Eurekaimer",
    profile: "https://github.com/Eurekaimer",
    ogImage: "profile.jpg",
    lang: "en",
    timezone: "Asia/Shanghai",
    dir: "ltr",
  },
  posts: {
    perPage: 4,
    perIndex: 0,
    scheduledPostMargin: 15 * 60 * 1000,
  },
  features: {
    lightAndDarkMode: true,
    dynamicOgImage: false,
    showArchives: false,
    showBackButton: true,
    editPost: {
      enabled: false,
    },
    search: false,
  },
  socials: [
    {
      name: "github",
      url: "https://github.com/Eurekaimer",
      linkTitle: "Eurekaimer on GitHub",
    },
    {
      name: "wechat",
      url: "https://cdn.jsdelivr.net/gh/Eurekaimer/TOUKO-IMGBED-03@main/objects/default/sha256/5d/1b/5d1b2acb60b28b5ced86642d0b84d88dc074db0aca4ddbdcf697a4d4e4a375c0.jpg",
      linkTitle: "WeChat QR code",
    },
    {
      name: "bilibili",
      url: "https://space.bilibili.com/702046230?spm_id_from=333.1007.0.0",
      linkTitle: "Eurekaimer on Bilibili",
    },
    {
      name: "qq",
      url: "https://cdn.jsdelivr.net/gh/Eurekaimer/TOUKO-IMGBED-04@main/objects/default/sha256/8c/3f/8c3f2287f2b148e2aaacd27dc73a91ae62148fec5ca8d91d6542e71af7563059.png",
      linkTitle: "QQ QR code",
    },
    {
      name: "mail",
      url: "mailto:2507983039@qq.com",
      linkTitle: "Email Eurekaimer",
    },
  ],
  shareLinks: [],
});

