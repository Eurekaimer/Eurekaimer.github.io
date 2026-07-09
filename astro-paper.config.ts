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
      url: "https://raw.githubusercontent.com/Eurekaimer/MyIMGs/refs/heads/main/img/Wechat.jpg",
      linkTitle: "WeChat QR code",
    },
    {
      name: "bilibili",
      url: "https://space.bilibili.com/702046230?spm_id_from=333.1007.0.0",
      linkTitle: "Eurekaimer on Bilibili",
    },
    {
      name: "qq",
      url: "https://raw.githubusercontent.com/Eurekaimer/MyIMGs/refs/heads/main/img/QQ.png",
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

