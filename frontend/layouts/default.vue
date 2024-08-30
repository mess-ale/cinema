<template>
    <div>
        <header :style="{ backgroundColor: headerBackgroundColor }"
            class="fixed top-0 left-0 right-0 z-10 w-full flex items-center justify-between text-white border-b border-gray-600 heading">
            <div class="flex items-center  space-x-10 font-bold">
                <dvi class="flex items-center space-x-2">
                    <img src="../static/images/logo.png" alt="company logo" class="w-10 h-10" />
                    <nuxt-link to="/" class="font-bold text-2xl">CineEthio</nuxt-link>
                </dvi>
                <div class="searchbox flex items-center border border-gray-300 rounded-lg overflow-hidden">
                    <div class="pl-3">
                        <svg class="w-5 h-5 text-gray-400" fill="currentColor" viewBox="0 0 20 20"
                            xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd"
                                d="M12.9 14.32a8 8 0 111.414-1.414l3.82 3.82a1 1 0 01-1.415 1.415l-3.82-3.82zM8 14A6 6 0 108 2a6 6 0 000 12z"
                                clip-rule="evenodd"></path>
                        </svg>
                    </div>
                    <input type="text" @input="filterMovies" placeholder="Search Movies..." class="inputclass" />
                    <nuxt-link class="pl-2 pr-2 font-bold" to="/filters">filter</nuxt-link>
                </div>
                <nuxt-link to="/movie" class="hover:text-gray-300">Movies</nuxt-link>
                <nuxt-link to="/What" class="hover:text-gray-300">What's On</nuxt-link>
                <nuxt-link to="/about" class="hover:text-gray-300">about</nuxt-link>
            </div>

            <div class="flex items-center">
                <div><nuxt-link v-if="true" to="/login">
                        <div onclick=""
                            class="get-tickets-button rounded-md flex items-center space-x-2 bg-secondary pt-1 pb-1 pl-3 pr-3 button">
                            Login
                            <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24">
                                <path fill="currentColor" fillRule="evenodd"
                                    d="M13.483 4.47a.75.75 0 0 1 1.06 0l6.988 7a.75.75 0 0 1 0 1.06l-6.988 7a.75.75 0 0 1-1.061-1.06l5.709-5.719L3 12.762a.75.75 0 0 1-.002-1.5l16.194-.01l-5.711-5.722a.75.75 0 0 1 0-1.06"
                                    clipRule="evenodd"></path>
                            </svg>
                        </div>
                    </nuxt-link>
                    <a v-else href="#" class="hover:text-gray-300">
                        <img src="" alt="Avatar" class="h-8 w-8 rounded-full">
                    </a>
                </div>

            </div>
        </header>

        <div class="bg-background text-white">
            <slot />
        </div>

        <footer class="bg-black text-white">
            <div class="footerpadding">
                <div class="footerlink flex">
                    <dvi class="flex items-center space-x-2">
                        <img src="../static/images/logo.png" alt="company logo" class="w-8 h-8" />
                        <nuxt-link to="/" class="font-bold text-xl">CineEthio</nuxt-link>
                    </dvi>

                    <div class="flex space-x-8">
                        <button class="socialM text-xl bg-red ">
                            <font-awesome-icon :icon="['fab', 'github']" /></button>
                        <button class="socialM text-xl bg-red ">
                            <font-awesome-icon :icon="['fab', 'linkedin']" /></button>
                        <button class="socialM text-xl bg-red ">
                            <font-awesome-icon :icon="['fab', 'facebook']" /></button>
                        <button class="socialM text-xl bg-red ">
                            <font-awesome-icon :icon="['fab', 'twitter']" /></button>
                    </div>
                </div>

                <div class="container mx-auto grid grid-cols-1 md:grid-cols-4 gap-8">
                    <div>
                        <p class="mb-4">Buy movie tickets easily with Aovis system nationwide</p>
                        <button class="get-tickets-button footer-button">
                            Get Your Ticket
                        </button>
                    </div>

                    <div>
                        <h4 class="text-orange-500 mb-4 font-bold">Movies</h4>
                        <ul class="space-y-2">
                            <li><a href="#" class="hover:text-orange-500">Action</a></li>
                            <li><a href="#" class="hover:text-orange-500">Adventure</a></li>
                            <li><a href="#" class="hover:text-orange-500">Animation</a></li>
                            <li><a href="#" class="hover:text-orange-500">Comedy</a></li>
                            <li><a href="#" class="hover:text-orange-500">Crime</a></li>
                        </ul>
                    </div>

                    <div>
                        <h4 class="text-orange-500 mb-4 font-bold">Links</h4>
                        <ul class="space-y-2">
                            <li><a href="#" class="hover:text-orange-500">About</a></li>
                            <li><a href="#" class="hover:text-orange-500">My account</a></li>
                            <li><a href="#" class="hover:text-orange-500">News</a></li>
                            <li><a href="#" class="hover:text-orange-500">Latest Events</a></li>
                            <li><a href="#" class="hover:text-orange-500">Contact</a></li>
                        </ul>
                    </div>

                    <div>
                        <h4 class="text-orange-500 mb-4 font-bold">Newsletter</h4>
                        <p class="mb-4">Subscribe to Leitmotif newsletter this very day.</p>
                        <div class="flex items-center space-x-2 mb-2">
                            <input type="email" placeholder="Email Address"
                                class="p-2 w-full rounded border border-gray-500 focus:outline-none focus:border-orange-500" />
                        </div>
                        <div class="flex items-center">
                            <input type="checkbox" id="agree"
                                class="form-checkbox text-orange-500 border-gray-500 rounded focus:ring-orange-500">
                            <label for="agree" class="ml-2 text-sm">I agree to all terms and policies of the
                                company</label>
                        </div>
                    </div>
                </div>
            </div>

            <div class="p-7 textcopy">
                <h1 class="text-center">© Copyright 2023 by CineEthio.com</h1>
            </div>
        </footer>
    </div>
</template>

<script>
export default {
    data() {
        return {
            headerBackgroundColor: 'transparent'
        };
    },
    mounted() {
        window.addEventListener('scroll', this.handleScroll);
    },
    destroyed() {
        window.removeEventListener('scroll', this.handleScroll);
    },
    methods: {
        handleScroll() {
            if (window.scrollY > 100) {
                this.headerBackgroundColor = '#000';
            } else {
                this.headerBackgroundColor = 'transparent';
            }
        }
    }
};
</script>

<style>
.button {
    cursor: pointer;
}

.search {
    cursor: pointer;
}

.heading {
    height: 6rem;
    padding: 0 2rem;
}

.container {
    padding: 5rem 0;
}

.get-tickets-button {
    background-color: theme('colors.primary');
    color: theme('colors.background');
    padding: 10px 20px;
    font-size: 1.2rem;
    font-weight: bold;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.get-tickets-button:hover {
    background-color: theme('colors.background');
    color: theme('colors.primary');
}

.footer-button {
    font-size: 0.8rem;
    border-radius: 1px;
}

.inputclass {
    border-width: 2px;
    width: 25rem;
    border: none;
    padding: 0.5rem 1rem;
    outline: none;
    background-color: transparent;
}

.searchbox {
    border: 2px solid theme('colors.primary');
}

.searchbox:focus-within {
    background-color: theme('colors.secondary');
}

.textcopy {
    background-color: #181818;
}

.footerlink {
    justify-content: space-between;
    padding: 1.75rem 0;
    border-bottom: 2px solid #181818;
}

.footerpadding {
    padding: 0 10rem;
}

.socialM {
    border-radius: 50%;
    background-color: #181818;
    padding: 1.25rem;
    transition: transform .3s ease-in-out;
}

.socialM:hover {
    transform: translateY(-15%);
    background-color: theme('colors.primary');
}

.socialM::after {
    transition: transform .3s ease-in-out;
}
.social-icons {
  display: flex;
  gap: 10px;
}
</style>
